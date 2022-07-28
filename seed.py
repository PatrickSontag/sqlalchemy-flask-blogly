"""Seed file to make sample data for db"""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.add_all()

# Add data to tables
fred = User(first_name="Fred", last_name="Durst", image="https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2018/09/640/320/vet_durst.jpg?ve=1&tl=1")
dan = User(first_name="Dan", last_name="Quinn", image="https://s.yimg.com/ny/api/res/1.2/JrZxu4tI2fzxTjLqz6WMog--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://s.yimg.com/os/creatr-uploaded-images/2021-12/9123d7e0-69c2-11ec-9b3f-d3605ec744e4")
ron = User(first_name="Ron", last_name="Swanson", image="https://pbs.twimg.com/profile_images/1262480275/ron-swanson-250fp011911_400x400.jpg")

p1 = Post(title="Greetings", content="Chocolate covered starfish.", created_at="2022-07-28", user_id="1")
p2 = Post(title="My first post", content="I coach football.", created_at="82022-07-28", user_id="2")
p3 = Post(title="Hello", content="All the eggs and bacon.", created_at="2022-07-28", user_id="3")

# Add users to db session and commit
db.session.add(fred)
db.session.add(dan)
db.session.add(ron)

db.session.commit()

# Add posts to db session and commit
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

db.session.commit()