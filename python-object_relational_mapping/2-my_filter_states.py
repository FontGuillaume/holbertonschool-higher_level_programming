#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> <mysql password>
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

    # Create cursor, format query with user input and execute
    cursor = db.cursor()
    name_search = sys.argv[4]
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        name_search)
    cursor.execute(query)
    
    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
