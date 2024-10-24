from flask import render_template, request, redirect, url_for, current_app

from .akeyless_integration import get_db

def init_app(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            if 'add' in request.form:
                add_todo(request.form['todo'])
            elif 'delete' in request.form:
                delete_todo(request.form['delete'])
            return redirect(url_for('index'))

        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM todos")
            todos = cursor.fetchall()
            cursor.close()
            return render_template('index.html', todos=todos)
        except Exception as e:
            return f"An error occurred: {e}"

def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    print(f"Cursor type: {type(cursor)}")
    cursor.execute('SELECT * FROM todos')
    print(f"Cursor description: {cursor.description}")
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return todos

def add_todo(todo):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO todos (task) VALUES (%s)', (todo,))
    db.commit()
    cursor.close()

def delete_todo(todo_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM todos WHERE id = %s', (todo_id,))
    db.commit()
    cursor.close()

print("Routes module loaded")
