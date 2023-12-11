# Group 2
# Module 11.1 Assignment
# 12/05/23

import mysql.connector
from mysql.connector import errorcode
import datetime

config = {
    "user": "root",
    "password": "",  # Insert Password
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

# Prints locations and their number of bookings by using SQL data
def printBookingsByLocation(title, rows):

    print("\n" + title)

    for row in rows:
        print(f"{row[1]}: {row[0]}")


# Make connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # Report welcome message
    print("Report 2")
    print("Description: Upcoming Bookings vs. Future Bookings by Location")

    # Execute query to display upcoming bookings
    cursor.execute("SELECT COUNT(booking_id), location.location_name FROM booking RIGHT JOIN trip ON trip.trip_id = booking.trip_id AND YEAR(trip.trip_startDate) = YEAR(CURRENT_DATE)+1 RIGHT JOIN location ON trip.location_id = location.location_id GROUP BY location.location_id;")

    rows = cursor.fetchall()

    current_year = datetime.date.today().year

    printBookingsByLocation(f"Upcoming Bookings ({current_year+1})", rows)

    # Execute query to display future bookings
    cursor.execute("SELECT COUNT(booking_id), location.location_name FROM booking RIGHT JOIN trip ON trip.trip_id = booking.trip_id AND YEAR(trip.trip_startDate) = YEAR(CURRENT_DATE)+2 RIGHT JOIN location ON trip.location_id = location.location_id GROUP BY location.location_id;")

    rows = cursor.fetchall()

    printBookingsByLocation(f"Future Bookings ({current_year+2})", rows)



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
