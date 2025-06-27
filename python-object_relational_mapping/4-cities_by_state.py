#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create cursor and execute join query to get cities with state names
    cursor = db.cursor()
    cursor.execute()

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
