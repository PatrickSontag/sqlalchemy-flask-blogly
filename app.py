"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

# db.create_all()
# Creates all tables from python Models file.  Should not need to create tables very often.  Can call from terminal or ipython rather than hard-coding.

@app.route('/')
def home_page():
    """Shows home page"""

    users = User.query.all()

    return render_template('home.html', users=users)

@app.route('/', methods=["POST"])
def add_user():
    """Shows home page"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    url = request.form['profile_picture']

    user = User(first_name=first_name, last_name=last_name, image_url=url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")

@app.route("/user/<int:user_id>")
def show_user(user_id):
    """Show info on user"""

    user = User.query.get_or_404(user_id)
    return render_template("user.html", user=user)

@app.route('/add')
def add_user_form():
    """Shows add user form"""
    return render_template('add_user.html')

@app.route('/edit/<int:user_id>')
def edit_user_form(user_id):
    """Shows current user info and edit user form"""

    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/update/<int:user_id>', methods=["POST"])
def update_user(user_id):
    """Update user info"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    url = request.form['profile_picture']

    user = User.query.get(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = url

    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")