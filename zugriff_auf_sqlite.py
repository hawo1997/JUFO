#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


con = lite.connect('JUFO.db')

with con:

    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM rasp1")

    rows = cur.fetchall()
    for row in rows:
        #print "%s %s %s" % (row["Raumnr"], row["Raumname"], row["Oeffnungszeiten"])
