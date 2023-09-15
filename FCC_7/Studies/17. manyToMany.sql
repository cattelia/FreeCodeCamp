In 16. we worked on One-to-Many, which is generally showed as a single arrow.
In 17. we are going to be working on Many-to-Many relationships, which is shown by a double arrow.

These are "data models"

Course: title << -- >> User: name, email

Many course could be going to many different students
while
many different students could be going to many courses

Course:
id
title

Member:
user_id (User.id)
course_id (Course.id)

User:
id
name
email

Complexity Enables Speed
- Complexity makes speed possible and allows you to get very fast results as the data grows in size.
- By normalizing the data and linking it with integer keys, the overall amount of data which the RDB must SCAN is far lower than if the data were simply flattened out.
- It might seem like a trade-off spend some time designing your DB so it continues to be fast when your application is a success
(In reality, you cannot read/write sequentially as you scale.)

Additional SQL Topics:
1. Indexes improve access performance for things like string fields
2. Constraints on data - (cannot be NULL)
3. Transactions - allow SQL operations to be grouped and done as a unit

Member is what we call the 'connector table'.


#=== Create Tables ===#
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) ;

#=== Insert Data ===#
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

#=== Foreign Membership Data ===#
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

#=== Looking at the Data ===#
SELECT User.name, Member.role, Course.title
  FROM User JOIN Member JOIN Course
  ON Member.user_id = User.id AND Member.course_id = Course.id
  ORDER BY Course.title, Member.role DESC, User.name 