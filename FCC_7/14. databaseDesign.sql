Complex Data Models

What if we have multiple tables?
Database Design

    Database design is an artform of its own.
    Goal: to avoid teh really bad mistakes and design clean and easily understood databases
    Others may performance tune things later
    

The act of figuring out the data that your application is going to want to store and spreading that through multiple tables.
Database design starts with a picture...

    This picture is of objects for our application and then figuring out how to represent the objects and their Relationships
    Basic rule:
        Dont put the same string in data twice - use a relationship instead
    When there is one thing in the "real world" there should be one copy of that thing in the Database

For each piece of info, ask yourself:
    1. Is the column an obj or attribute of another object?
    2. Once we define objects, we need to define the relationship between objects

What is this application about?
What is this TRACKING?

===============================================================================================================================

Database Normalization (3NF)

    Do not replicate data - reference data - point at data, but do not replicate
    Use integer for keys and for reference
    Add a special "key" column to each table which we will make references to. By convention: this is "id"


Integer Reference Pattern - 
    Best Practice:
        Never use your logical key as the primary key
        Logical key can and od change, albiet slowly
        Relationships that are based on matching strings are less effective than integers

Example:
    #Primary key
    id      name
    1       Led Zepplin
    2       AC/DC

            #Foreign key
    id      artist_id   title
    1       2           Who Made Who  
    2       1           IV

Three Kinds of keys
    1. Primary key - generally an integer auto-increment field
    2. Logical key - what the outside world uses
    3. Foreign key - generally an integer key pointing to a row in ANOTHER table

===============================================================================================================================



