
    id integer primary key autoincrement,
    username string not null,
    firstname string not null,
    lastname string not null,
    email string not null,
    password string not null,
    likes integer default(0),
    matches integer default(0),
    bio text default('Tell everyone about yourself...'),
    gender string,
    sex_orientation string,
    fame integer default(0),
    geo_location string,
    last_online string,
    complete string default(FALSE),

INSERT INTO users(email, username, firstname, lastname, password,  gender, last_online) VALUES (
    'root@root.com', 'root', 'rootie', 'tootie', 'Qwert2@', 'Male', 'Never',)