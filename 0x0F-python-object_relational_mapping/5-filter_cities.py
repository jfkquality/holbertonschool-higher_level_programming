#!/usr/bin/python3
""" List all states in database table """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    myuser = argv[1]
    mypwd = argv[2]
    mydb = argv[3]
    statesearch = argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=myuser,
                         passwd=mypwd,
                         db=mydb)

    cur = db.cursor()

    sql = "SELECT c.id, c.name, s.name \
      FROM cities AS c \
      INNER JOIN states as s ON c.state_id = s.id \
      ORDER BY c.id"

    cur.execute(sql)

    print(', '.join(cname for id, cname, sname in cur.fetchall()
                    if sname == statesearch))

    cur.close()
    db.close()
