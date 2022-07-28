DROP DATABASE IF EXISTS blogly;

CREATE DATABASE blogly;

\c blogly;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    image TEXT
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    created_at DATE,
    user_id INTEGER REFERENCES users(id)
);

INSERT INTO users
    (first_name, last_name, image)
VALUES
    ('Fred', 'Durst', 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2018/09/640/320/vet_durst.jpg?ve=1&tl=1'),
    ('Dan', 'Quinn', 'https://s.yimg.com/ny/api/res/1.2/JrZxu4tI2fzxTjLqz6WMog--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://s.yimg.com/os/creatr-uploaded-images/2021-12/9123d7e0-69c2-11ec-9b3f-d3605ec744e4'),
    ('Ron', 'Swanson', 'https://pbs.twimg.com/profile_images/1262480275/ron-swanson-250fp011911_400x400.jpg');

INSERT INTO posts
    (title, content, created_at, user_id)
VALUES
    ('Greetings', 'Chocolate covered starfish.', '2022-07-28', 1),
    ('My first post', 'I coach football.', '2022-07-28', 2),
    ('Hello', 'All the eggs and bacon.', '2022-07-28', 3);

SELECT * FROM users
    JOIN posts
    ON users.id = posts.user_id;