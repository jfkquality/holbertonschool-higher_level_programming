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
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    cur.execute(sql)

    for id, name in cur.fetchall():
        if name.startswith('N'):
            print("({}, '{}')".format(id, name))

    cur.close()
    db.close()
