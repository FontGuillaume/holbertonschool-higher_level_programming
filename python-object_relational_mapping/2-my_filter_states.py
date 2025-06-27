#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    name_search = sys.argv[4]
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name_search)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
