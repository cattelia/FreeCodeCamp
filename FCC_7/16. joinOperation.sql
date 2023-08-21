Using Join Across tables

Relational Power:
By removing the replicated data and replacing it with references to a single copy of each bit
of data we build a "web" of information that the RDB can read through quickly.
EVEN through very large data.

JOIN Operation

This operations links across several tables as part of a select operations
You must tell the JOIN 'how to use the keys' that make the connection 
between the tables using an ON clause.


SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
       -----------------------       -----      ------    --------------------------
       What we want to see           The tables needed       How the tables are linked

When ON Clause is not used, things go wrong.
'ON the DB Dashboard you will see that using a Join command without the ON clause will
return all possible combinations of rows.'

Joining from Multiple tables, let us break down th
SELECT 

Track.title, Artist.name, Album.title, Genre.name (The columns I want)

FROM Track (Establish main view where pointers 'start')
JOIN Genre JOIN Album JOIN Artist (Join/connect the other tables)

    ON Track.genre_id = Genre.id (tells where the pointers 'go') (In this case, Grabs Track.genre_id, goes to Genre table and grabs Genre.id and tells pointer: here is your information)
    AND Track.album_id = Album.id (AND this one as well.)
    AND Album.artist_id = Artist.id (And this one.)


#=== JOIN || ON  Commands ===#

SELECT Album.title, Artist.name FROM Album JOIN Artist 
    ON Album.artist_id = Artist.id

SELECT Album.title, Album.artist_id, Artist.id, Artist.name 
    FROM Album JOIN Artist ON Album.artist_id = Artist.id

#=== JOIN without ON clause ===#

SELECT Track.title, Track.genre_id, Genre.id, Genre.name 
    FROM Track JOIN Genre   

#=== Showing Duplicated Data ===#

SELECT Track.title, Genre.name FROM Track JOIN Genre 
    ON Track.genre_id = Genre.id

#=== JOIN from Multiple Tables ===#

SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id