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
