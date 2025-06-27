#!/usr/bin/python3
"""
Script that displays values safely from the states table where name matches.
This script prevents SQL injection by using parameterized queries.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password>
                                   <database name> <state name searched>
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

    # Create cursor and execute parameterized query to prevent SQL injection
    cursor = db.cursor()
    name_search = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (name_search,))
    
    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
