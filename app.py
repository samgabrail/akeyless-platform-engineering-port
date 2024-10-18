from flask import Flask, render_template
import mysql.connector
import os
import json

app = Flask(__name__)

def get_db_connection():
    with open('/secrets/db-creds.json') as f:
        creds = json.load(f)
    
    return mysql.connector.connect(
        host=os.environ['DB_HOST'],
        user=creds['username'],
        password=creds['password'],
        database=os.environ['DB_NAME']
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tables=tables)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

