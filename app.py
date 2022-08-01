"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag, user_posts_join_class

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


def handle_user_image(user, default_image='https://icon-library.com/images/default-user-icon/default-user-icon-13.jpg'):
    if not user.image:
        user.image = default_image
    return user

@app.route('/')
def home_page():
    """Shows home page"""

    # users = []
    # for user in User.query.all():
    #     users.append(handle_user_image(user))
    posts = Post.query.all()

    tags = []
    for i, p in enumerate(posts):
        tags.append(posts[i].ts)
    
    return render_template('home.html', posts=posts, tags=tags)

@app.route('/users')
def users():
    """Shows home page"""

    users = []
    for user in User.query.all():
        users.append(handle_user_image(user))
    return render_template('users.html', users=users)

@app.route('/', methods=["POST"])
def add_user():
    """Shows home page"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image = request.form['profile_picture']

    user = User(first_name=first_name, last_name=last_name, image=image)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")

@app.route("/user/<int:user_id>")
def show_user(user_id):
    """Show info on user"""

    user = User.query.get_or_404(user_id)
    posts = user.posts
    print("POSTS:::::::", posts)
    tags = []
    for i, p in enumerate(posts):
        tags.append(posts[i].ts)
    # tags = user.tags
    # tags = posts.tags
    # print("TAGS::::::::", tags)
    # posts = Post.query.filter_by(user.id=user_id)
    user = handle_user_image(user)

    return render_template("user.html", user=user, posts=posts, tags=tags)
    # tags=tags

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
    image = request.form['profile_picture']

    user = User.query.get(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image = image

    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")

@app.route('/delete/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    """Delete user"""

    User.query.filter_by(id=user_id).delete()

    db.session.commit()

    return redirect('/')

@app.route('/user/<int:user_id>/new_post')
def new_post_form(user_id):
    """Shows new post form"""
    user = User.query.get(user_id)
    tags = Tag.query.all()

    return render_template('new_post.html', user=user, tags=tags)

@app.route('/user/<int:user_id>/new_post', methods=["POST"])
def new_post(user_id):
    """Add new post"""
    
    title = request.form['title']
    content = request.form['content']
    # tags = request.form.getlist('tags')
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()


    print("1111111111111111- new post, tags: ", tags, "| tag_ids:, ", tag_ids)
    user = User.query.get(user_id)
    post = Post(title=title, content=content, user_id=user_id, tags=tags)
    
    db.session.add(post)
    db.session.commit()

    return redirect(f"/user/{user.id}")


@app.route('/delete/post/<int:post_id>', methods=["POST"])
def delete_post(post_id):
    """Delete post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f"/user/{post.user_id}")

@app.route('/edit/post/<int:post_id>')
def edit_post_form(post_id):
    """Shows edit post form"""
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    tags = Tag.query.all()
    return render_template('edit_post.html', post=post, user=user, tags=tags)