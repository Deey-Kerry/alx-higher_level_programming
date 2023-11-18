#!/usr/bin/python3
"""
a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument. But this time, write one
that is safe from MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access to the database of the states
    """
    conn = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = conn.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY \
                %(name)s ORDER BY id ASC", {'name': argv[4])
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
