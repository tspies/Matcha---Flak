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

drop table if exists interests ;
create table interests(
    id integer primary key autoincrement,
    username string not null,
    travelling  integer default(0),
    exercise    integer default(0),
    movies      integer default(0),
    dancing     integer default(0),
    cooking     integer default(0),
    outdoors    integer default(0),
    politics    integer default(0),
    pets        integer default(0),
    photography integer default(0),
    sports      integer default(0)
);

drop table if exists likes ;
create table likes(
    id integer primary key autoincrement,
    user_liking string not null,
    user_liked string not null
);

drop table if exists matches;
create table matches(
    id integer primary key autoincrement ,
    user_1 string not null,
    user_2 string not null
);
