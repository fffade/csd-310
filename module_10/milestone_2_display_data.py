# Group 2
# Module 10.1 Assignment
# 12/02/23

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "",  # Insert Password
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}


# Displays a table regularly in the database
def show_table(cursor, table_name):
    # query
    cursor.execute("SELECT * FROM {};".format(table_name))

    # get results using cursor
    rows = cursor.fetchall()

    # get column names
    col_names = [i[0] for i in cursor.description]

    # display title
    print("\n -- Displaying {} --".format(table_name))

    # display column names
    print("  |  ".join(col_names))

    # iterate over data set and show
    for row in rows:
        print(row)


# Display a customized output for a table using column names
def show_table_customized(cursor, table_name, title, column_names):
    # query
    cursor.execute("SELECT * FROM {};".format(table_name))

    # get results using cursor
    rows = cursor.fetchall()

    # display title
    print("\n -- Displaying {} --".format(title))

    # iterate over each entry and display fit to given column names
    for row in rows:

        col_index = 0
        for column in row:
            # display column name alongside entry value
            print("{}: {}".format(column_names[col_index], column.__str__()))

            col_index += 1

        print("")


# Make connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # Show all customers
    show_table_customized(cursor, "customer", "Customers",
                          ("ID", "Last Name", "First Name", "Email Address"))

    print()

    # Show all trips
    show_table_customized(cursor, "trip", "Trips",
                          ("ID", "Name", "Price", "Length", "Start Date", "Location ID", "Guide ID"))

    print()

    # Show all locations
    show_table_customized(cursor, "location", "Locations",
                          ("ID", "Name"))

    print()

    # Show all guides
    show_table_customized(cursor, "guide", "Guides",
                          ("ID", "First Name", "Last Name"))

    print()

    # Show all bookings
    show_table_customized(cursor, "booking", "Bookings",
                          ("ID", "Date", "Customer ID", "Trip ID"))

    print()

    # Show all equipment orders
    show_table_customized(cursor, "equipment_order", "Equipment Orders",
                          ("ID", "Date", "Quantity", "Total"))

    print()

    # Show all equipment inventory
    show_table_customized(cursor, "equipment", "Equipment Inventory",
                          ("ID", "Name", "Order ID"))

    print()

    # Show all rentals and purchases
    show_table_customized(cursor, "equipment_rental", "Equipment Rentals",
                          ("ID", "Rental Start Date", "Rental End Date", "Rental Total", "Customer ID", "Equipment ID"))

    print()

    show_table_customized(cursor, "equipment_purchase", "Equipment Purchases",
                          ("ID", "Purchase Date", "Quantity", "Total", "Customer ID", "Equipment ID"))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
