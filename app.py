import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from database import db
from user import User


app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///stop_hate.db'
app.secret_key = os.getenv("SECRET_KEY")
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route("/")
def main():
    return render_template("index.html")




# Assuming you have a user loader and User class defined
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# Route to render the login form
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


# Route to handle the login form submission
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    # Here, implement your authentication logic, e.g., check username and password
    user = User.authenticate(username, password)  # This is just a placeholder; implement your method

    if user:
        login_user(user)
        return redirect(url_for('dashboard'))  # Redirect to a dashboard or other target page after login
    else:
        flash('Invalid username or password')
        return redirect(url_for('login'))


# Route for the dashboard or other protected page
@app.route('/dashboard')
@login_required
def dashboard():
    return 'You are logged in'


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('index'))

@app.route("/user-media")
@login_required
def user_media():
    return render_template("user-media.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

