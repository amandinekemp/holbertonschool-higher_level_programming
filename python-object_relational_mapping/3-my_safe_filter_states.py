#!/usr/bin/python3
"""This script connects to a MySQL database and displays the values in the
'states' table, where the name corresponds exactly to the input argument. """

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = \
                   %s;", ((argv[4], )))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close
    cursor.close
