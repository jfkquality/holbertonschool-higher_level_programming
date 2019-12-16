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

    sql = "SELECT c.id, c.name, s.name \
      FROM states AS s \
      INNER JOIN cities as c ON s.id = c.state_id"

    cur.execute(sql)

    for row in cur.fetchall():
        # if name == statesearch:
        print(row)
        # print("({}, '{}', '{}')".format(id, name, name))

    cur.close()
    db.close()
