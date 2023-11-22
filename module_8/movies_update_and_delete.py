# Omar Johnson
# Module 8.2 Assignment
# 11/22/23

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Lo21!#21",  # Password redacted for security reasons
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


# Displays all the films from the 'movies' database
def show_films(cursor, title):
    # method to execute an inner join on all tables and interate over the dataset to output results

    # inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film " +
                   "INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

    # get results using cursor
    films = cursor.fetchall()

    # display title
    print("\n -- {} --".format(title))

    # iterate over data set and show
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


# Make connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # Show all films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert new film
    cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) " +
                   "VALUES ('The Revenant', '2015', 156, 'Alejandro González Iñárritu', 1, 1)")

    # Show films again
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update the film 'Alien'
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")

    # Show films again
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete 'gladiator'
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

    # Show films again
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")

    else:
        print(err)

finally:
    db.close()