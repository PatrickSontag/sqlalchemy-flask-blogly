DROP DATABASE IF EXISTS blogly;

CREATE DATABASE blogly;

\c blogly;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    image TEXT
);

INSERT INTO users
    (first_name, last_name, image)
VALUES
    ('Fred', 'Durst', '/user_profile_pics/fred_durst.jpg'),
    ('Larry', 'McVerde', '/user_profile_pics/larry_mcverde.jpg'),
    ('Ronald', 'Weasley', '/user_profile_pics/ronald_weasley.jpg');