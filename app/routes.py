from flask import render_template, request, redirect, url_for, current_app
import mysql.connector
import os
import json

def init_app(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            if 'add' in request.form:
                add_todo(request.form['todo'])
            elif 'delete' in request.form:
                delete_todo(request.form['delete'])
            return redirect(url_for('index'))

        todos = get_todos()
        return render_template('index.html', todos=todos)

def get_db_connection():
    try:
        # Try to read credentials from Akeyless-injected file first
        if os.path.exists('/secrets/db-creds.json'):
            with open('/secrets/db-creds.json') as f:
                creds = json.loads(f.read())
                username = creds['username']
                password = creds['password']
                print(f"Using Akeyless credentials for user: {username}")
        else:
            # Fall back to environment variables for local development
            username = os.environ.get('DB_USERNAME', 'myuser')
            password = os.environ.get('DB_PASSWORD', 'mypassword')
            print("Using fallback credentials")

        host = os.environ.get('DB_HOST', 'localhost')
        database = os.environ.get('DB_NAME', 'todos')
        
        print(f"Attempting to connect to MySQL - Host: {host}, Database: {database}, User: {username}")
        
        return mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
    except Exception as e:
        current_app.logger.error(f"Error connecting to database: {str(e)}")
        raise

def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return todos

def add_todo(todo):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (task) VALUES (%s)', (todo,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_todo(todo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = %s', (todo_id,))
    conn.commit()
    cursor.close()
    conn.close()

print("Routes module loaded")
