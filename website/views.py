from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/profile')
def profile():
    return render_template("profile.html")

@views.route('/alxstorieswrite')
def write():
    return render_template('alxstorieswrite.html')

@views.route('/alxstoriesread')
def read():
    return render_template("alxstoriesread.html")