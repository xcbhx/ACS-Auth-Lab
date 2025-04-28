from flask import Flask
from books_app.extensions import db, login_manager, bcrypt
from books_app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'

    from books_app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # careful to wrap user_id as int

    # Import and register blueprints
    from books_app.main.routes import main
    from books_app.auth.routes import auth  # if you have an auth blueprint
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app