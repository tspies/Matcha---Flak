drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username string not null,
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
    verified string default(FALSE)
);
