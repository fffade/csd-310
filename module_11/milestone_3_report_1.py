# Group 2
# Module 11.1 Assignment
# 12/05/23

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "",  # Insert Password
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}


# Make connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # Report welcome message
    print("Report 1")
    print("Description: Equipment Orders vs. Equipment Sales")

    # Execute query to display equipment orders
    cursor.execute("SELECT SUM(order_total) AS 'Equipment Orders Total' FROM equipment_order;")

    row = cursor.fetchall()[0]
    orders_total = row[0]

    print(f"\nTotal of all orders: ${orders_total}")

    # Execute query to display equipment sales
    cursor.execute("SELECT (SUM(purchase_total) + SUM(rental_total)) AS 'Equipment Sales Total' FROM equipment_purchase JOIN equipment_rental;")

    row = cursor.fetchall()[0]
    sales_total = row[0]

    print(f"Total of all sales (incl. rentals & purchases): ${sales_total}")

    # Print summary message
    if orders_total > sales_total:
        print("\nOrder expenses EXCEEDS customer sales!")
    else:
        print("\nOrder expenses is less than or equivalent to customer sales")



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
