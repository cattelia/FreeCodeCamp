Relationship Building in tables

Track:

id (Primary key)
title (Logical key)
rating
len
count
album_id (Foreign key to Album)

Album:

id (:album_id:)
title (Logical key)

Say we added another Table that we wanted to track information: Genre.
What happens? >>> Notice how Track: gains a new Foreign key to Genre by pointing at the Genre:id

Genre:

id (Primary key) (:genre_id:)
name (Logical key)

Track:

id (Primary key)
title (Logical key)
rating
len
count
album_id (Foreign key to Album:)
genre_id (Foreign key to Genre:)

Album:

id (Primary key) (:album_id:)
title (Logical key)


#===Multi-Table SQL===#

CREATE TABLE "Artist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    artist_id INTEGER,
    "title" TEXT)

CREATE TABLE "Genre" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, 
    "title" TEXT, "count" INTEGER)

#=== Filling Multi-tables ===#

INSERT INTO Artist (name) VALUES ('Led Zepplin')
INSERT INTO Artist (name) VALUES ('AC/DC')

INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal');


#=== Establishing Foreign keys ===#
Notice how Album requires both title and artist_id, where artist_id is the foreign key

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);


#=== Establishing Multiple Foreign keys ===#

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;