#!/usr/bin/python3
"""
Module 5-filter_cities
Takes in the name of a state as an argument and lists all cities of that state.
Uses direct MySQL database connection to filter cities by state name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute(""" SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name = '{}';
                """.format(sys.argv[4].replace("'", "''")))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    if rows:
        print(", ".join(city[0] for city in rows))
    else:
        print()

    # Close the cursor and the database connection
    cur.close()
    db.close()
