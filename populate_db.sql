--
--     id integer primary key autoincrement,
--     username string not null,
--     firstname string not null,
--     lastname string not null,
--     email string not null,
--     password string not null,
--     likes integer default(0),
--     matches integer default(0),
--     bio text default('Tell everyone about yourself...'),
--     gender string,
--     sex_orientation string,
--     fame integer default(0),
--     geo_location string,
--     last_online string,
--     complete string default(FALSE),

INSERT INTO users(email, username, firstname, lastname, password,  gender, last_online, verified) VALUES ('Ruth@matcha.com', 'Ruth', 'Swart', 'Swart', '$2b$12$T/ENjvPLY4p.beWVlWjGOe/6j0h2agDbFYA.Hub9DilAKzExtkJeq', 'Female', 'Never', 1);
INSERT INTO interests (username) VALUES ('Ruth');

INSERT INTO users(email, username, profile_pic, firstname, lastname, password,  gender, last_online, verified) VALUES ('Mushu@matcha.com', 'Mushu', 'havana_profile.jpg', 'Spies', 'Spies', '$2b$12$T/ENjvPLY4p.beWVlWjGOe/6j0h2agDbFYA.Hub9DilAKzExtkJeq', 'Female', 'Never', 1);
INSERT INTO interests (username) VALUES ('Mushu');
INSERT INTO images (username, file_name) VALUES ('Mushu', 'havana_profile.jpg'), ('Mushu', 'havana1.jpg'),  ('Mushu', 'havana2.jpg');

INSERT INTO users(email, username, firstname, lastname, password,  gender, last_online, verified) VALUES ('Leyla@matcha.com', 'Leyla', 'Esterhuizen', 'Esterhuizen', '$2b$12$T/ENjvPLY4p.beWVlWjGOe/6j0h2agDbFYA.Hub9DilAKzExtkJeq', 'Female', 'Never', 1);
INSERT INTO interests (username) VALUES ('Leyla');

INSERT INTO users(email, username, firstname, lastname, password,  gender, last_online, verified) VALUES ('Daniell@matcha.com', 'Daniell', 'Daniell', 'Esterhuizen', '$2b$12$T/ENjvPLY4p.beWVlWjGOe/6j0h2agDbFYA.Hub9DilAKzExtkJeq', 'Male', 'Never', 1);
INSERT INTO interests (username) VALUES ('Daniell');

INSERT INTO users(email, username, firstname, lastname, password,  gender, last_online, verified) VALUES ('Zaza@matcha.com', 'Zaza', 'Zaza', 'Bronkie', '$2b$12$T/ENjvPLY4p.beWVlWjGOe/6j0h2agDbFYA.Hub9DilAKzExtkJeq', 'Female', 'Never', 1);
INSERT INTO interests (username) VALUES ('Zaza');

INSERT INTO users(email, username, firstname, lastname, password,  gender, last_online, verified) VALUES ('Rein@matcha.com', 'Rein', 'Reinhardt', 'Bronkie', '$2b$12$T/ENjvPLY4p.beWVlWjGOe/6j0h2agDbFYA.Hub9DilAKzExtkJeq', 'Male', 'Never', 1);
INSERT INTO interests (username) VALUES ('Rein');