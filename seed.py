"""Seed file to make sample data for db"""

from models import User, Post, Tag, PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add data to tables
nate = User(first_name="Nate", last_name="Nickerson", image="https://www.looper.com/img/gallery/the-office-star-you-forgot-appeared-on-better-call-saul/nate-from-the-office-recurs-as-pryce-in-better-call-saul-1640030469.jpg")
charles = User(first_name="Charles", last_name="Boyle", image="https://writingwinters.com/wp-content/uploads/boyle.jpg")
ron = User(first_name="Ron", last_name="Swanson", image="https://pbs.twimg.com/profile_images/1262480275/ron-swanson-250fp011911_400x400.jpg")

p1 = Post(title="Ryan vs Ravi", content="I've never met Ravi personally, but I'm gonna go ahead and say just having known you a short while, Brian, that I prefer Ravi.  And again, I've never even met the guy.", created_at="2022-07-28", user_id="1")
p2 = Post(title="Influence", content="I've never been a bad influence on anyone.", created_at="2022-07-28", user_id="2")
p3 = Post(title="Hello", content="All the eggs and bacon.", created_at="2022-07-28", user_id="3")

t1 = Tag(name="Work")
t2 = Tag(name="Travel")
t3 = Tag(name="Fun")
t4 = Tag(name="Music")

pt1 = PostTag(posts_id=1, tag_id=1)
pt2 = PostTag(posts_id=1, tag_id=4)
pt3 = PostTag(posts_id=2, tag_id=1)
pt4 = PostTag(posts_id=2, tag_id=3)
pt5 = PostTag(posts_id=3, tag_id=3)

# Add users and tags to db session and commit
db.session.add(nate)
db.session.add(charles)
db.session.add(ron)
db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)

db.session.commit()

# Add posts to db session and commit
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

db.session.commit()

# Add posttags to db session and commit
db.session.add(pt1)
db.session.add(pt2)
db.session.add(pt3)
db.session.add(pt4)
db.session.add(pt5)

db.session.commit()