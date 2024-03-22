#!/usr/bin/python3
"""This script takes as input an argument and displays all values in
the hbtn_0e_0_usa state table where the name matches the argument supplied"""

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
