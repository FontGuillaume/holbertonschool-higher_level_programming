#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <mysql username> <mysql password>
                           <database name> <state name>
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
    state_name = sys.argv[4]
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all rows and print them as a comma-separated list
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]  # Extract city names from rows
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
