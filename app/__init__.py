from flask import Flask
from .akeyless_integration import init_app as init_db

def create_app():
    app = Flask(__name__)
    
    # Initialize the database pool
    init_db(app)
    
    from app import routes
    routes.init_app(app)
    
    return app

