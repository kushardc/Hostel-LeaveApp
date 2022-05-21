from turtle import title
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')  # home page that return 'index'
def index():
    return render_template('base.html')


@main.route('/login.html')
@login_required
def login():
    return render_template('login.html')


@main.route('/profile.html')
def profile():
    return render_template("profile.html")

@main.route('/page4.html')
def page4():
    return render_template("page4.html")

@main.route('/thankyou.html')
def thankyou():
    return render_template("thankyou.html")



app = create_app()  # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
