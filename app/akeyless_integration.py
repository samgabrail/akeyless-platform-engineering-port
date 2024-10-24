import requests
import os
import mysql.connector
from flask import current_app
import time

# URLs for Akeyless Gateway
AUTH_URL = "https://192.168.1.82:8081/auth"
SECRET_URL = "https://192.168.1.82:8081/get-dynamic-secret-value"

# Load the service account token
def get_k8s_service_account_token():
    with open('/var/run/secrets/kubernetes.io/serviceaccount/token', 'r') as file:
        return file.read().strip()

# Authenticate with Akeyless using Kubernetes auth
def authenticate_with_akeyless():
    k8s_service_account_token = get_k8s_service_account_token()
    payload = {
        "access-type": "k8s",
        "json": True,
        "access-id": "p-trkddl1zvs2qkm",
        "debug": True,
        "gateway-url": "https://192.168.1.82:8000",
        "k8s-auth-config-name": "/demos/K8s-Auth-for-Demos",
        "k8s-service-account-token": k8s_service_account_token,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(AUTH_URL, json=payload, headers=headers, verify='/etc/ssl/certs/gateway_cert.pem')
    response.raise_for_status()
    return response.json().get('token')

# Retrieve the dynamic secret
def get_dynamic_secret(token):
    payload = {
        "json": True,
        "timeout": 15,
        "name": "/demos/mysql_root_password_dynamic",
        "target": "/demos/mysql_root_password_target",
        "token": token
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(SECRET_URL, json=payload, headers=headers, verify='/etc/ssl/certs/gateway_cert.pem')
    response.raise_for_status()
    return response.json()

# Get database connection using dynamic secret with retry mechanism
def get_db_connection(retries=3, delay=5):
    for attempt in range(retries):
        try:
            token = authenticate_with_akeyless()
            secret = get_dynamic_secret(token)
            username = secret['user']
            password = secret['password']
            host = os.environ.get('DB_HOST', 'localhost')
            database = os.environ.get('DB_NAME', 'todos')

            return mysql.connector.connect(
                host=host,
                user=username,
                password=password,
                database=database
            )
        except mysql.connector.Error as e:
            if "expired" in str(e).lower():
                current_app.logger.info("Dynamic secret expired, retrying...")
                time.sleep(delay)
            else:
                current_app.logger.error(f"Error connecting to database: {str(e)}")
                raise
    raise Exception("Failed to connect to the database after retries")
