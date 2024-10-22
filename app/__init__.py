from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app import routes
    routes.init_app(app)
    
    print("Registered routes:")
    print(app.url_map)
    
    return app

