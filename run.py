import os
from app import create_app

# Set environment variables for local development
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_NAME'] = 'myapp'
os.environ['DB_USERNAME'] = 'myuser'
os.environ['DB_PASSWORD'] = 'mypassword'

app = create_app()

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(host='0.0.0.0', port=8080, debug=True)
