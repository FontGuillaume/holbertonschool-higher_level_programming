#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
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

    # Create cursor and execute query to filter states starting with 'N'
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    
    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
