#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    myuser = argv[1]
    mypwd = argv[2]
    mydb = argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=myuser,
                         passwd=mypwd,
                         db=mydb)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for id, name in cur.fetchall():
        print("({}, '{}')".format(id, name))

    cur.close()
    db.close()
