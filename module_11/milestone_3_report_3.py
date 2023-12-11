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

# prints an equipment item given its row
def printEquipmentItem(row):
    print(f"{row[1]} (ID: {row[0]}) ({row[2]} days old)")

# Make connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # Variable deciding how old is 'too old'
    max_order_years = 5

    # Report welcome message
    print("Report 3")
    print(f"Description: Aged Equipment in Inventory (over {max_order_years} years)")

    # Execute query to fetch old equipment
    cursor.execute(f"SELECT equipment_id, equipment_name, TO_DAYS(CURRENT_DATE) - TO_DAYS(order_date) FROM equipment INNER JOIN equipment_order ON equipment.order_id = equipment_order.order_id WHERE TO_DAYS(CURRENT_DATE) - TO_DAYS(order_date) > 365 * {max_order_years};")

    rows = cursor.fetchall()

    # Display each item
    print("\nItems:")
    for row in rows:
        printEquipmentItem(row)

    print(f"\nThere are {len(rows)} inventory items exceeding max age.")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
