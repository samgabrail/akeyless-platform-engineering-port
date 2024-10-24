import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(host='0.0.0.0', port=8082, debug=True)
