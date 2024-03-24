import os
from flask import Flask
from flask_login import LoginManager
from database import db
from user import User


def create_app():
    app = Flask(__name__)
    app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///stop_hate.db'
    app.secret_key = os.getenv("SECRET_KEY")

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    with app.app_context():
        db.create_all()

    from routers import init_app_routes
    init_app_routes(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
