from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from user import User

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
        return render_template("user-media.html")


