import os

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from user import User
from instagram_basic_display_api import InstagramBasicDisplayAPI



def init_app_routes(app):
    @app.route("/")
    def main():
        return render_template("index.html")

    @app.route('/login', methods=['GET'])
    def login():
        return render_template('login.html')

    @app.route('/login', methods=['POST'])
    def login_post():
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("Username and password are required")
            return redirect(url_for("login"))

        user = User.authenticate(username, password)

        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash("You have been logged out.")
        return redirect(url_for('index'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return 'You are logged in'

    @app.route("/user-media")
    @login_required
    def user_media():
        code = request.args.get("code")
        try:
            ig_api = InstagramBasicDisplayAPI({
                "INSTAGRAM_APP_ID": os.getenv("INSTAGRAM_APP_ID"),
                "INSTAGRAM_APP_SECRET": os.getenv("INSTAGRAM_APP_SECRET"),
                "INSTAGRAM_APP_REDIRECT_URI": os.getenv("INSTAGRAM_APP_REDIRECT_URI")
            })
            if not code:
                ig_api.set_authorization_url()
                return redirect(ig_api.authorization_url)
            else:
                ig_api.set_user_instagram_access_token(code)
                user_media = ig_api.get_user_media()
                return render_template("user-media.html", media_data=user_media)
        except Exception as error:
            flash("An error occurred while trying to fetch Instagram data.")
            app.logger.error(f"Instagram Api error: {error}")
            return redirect(url_for("main"))

    @app.route("/my-page")
    @login_required
    def my_page():
        return render_template("my_page.html")


    @app.route("/some_endpoint")
    def some_endpoint():
        return render_template("some_endpoint.html")

    @app.route("/admin")
    @login_required
    def admin():
        if not current_user.is_authenticated or not current_user.is_admin:
            flash("Unauthorized access.")
            return redirect(url_for("main"))

        users = User.query.all()
        return render_template("admin", users=users)
