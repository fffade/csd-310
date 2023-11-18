# Omar Johnson
# Module 7.2 Assignment
# 11/18/23

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "",  # Password redacted for security reasons
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # Select and print all studios
    studio_query = "SELECT studio_id, studio_name FROM studio"

    cursor.execute(studio_query)

    studios = cursor.fetchall()

    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    # Select and print all genres
    genre_query = "SELECT genre_id, genre_name FROM genre"

    cursor.execute(genre_query)

    genres = cursor.fetchall()

    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # Select and print films with a runtime SHORTER than 2 hours
    film_query = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"

    cursor.execute(film_query)

    films = cursor.fetchall()

    print("-- DISPLAYING Film RECORDS --")
    for film in films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    # Select and director records ordered by director name
    director_query = "SELECT film_name, film_director FROM film ORDER BY film_director"

    cursor.execute(director_query)

    films = cursor.fetchall()

    print("-- DISPLAYING Director RECORDS in Order --")
    for film in films:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")

    else:
        print(err)

finally:
    db.close()