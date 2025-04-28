from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create db instance (this is what your models.py is trying to import)
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database.db'

    db.init_app(app)
    login_manager.init_app(app)

    # Import and register your blueprints/routes here
    from books_app.main.routes import main
    app.register_blueprint(main)

    return app
