#!/usr/bin/python3
""" List all states in database table """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    myuser = argv[1]
    mypwd = argv[2]
    mydb = argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=myuser,
                         passwd=mypwd,
                         db=mydb)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for id, name in cur.fetchall():
        print("({}, '{}')".format(id, name))

    cur.close()
    db.close()
