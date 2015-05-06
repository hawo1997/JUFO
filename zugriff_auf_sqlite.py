import sqlite3 as lite

def Auslesen(Nr):
    con = lite.connect('JUFO.db')
    with con:

        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM rasp1")

        rows = cur.fetchall()
        for row in rows:
            if Nr==row["Raumnr"]:
                print(row["Oeffnungszeiten"])
#            print(row["Raumnr"],row["Raumname"], row["Oeffnungszeiten"])

Auslesen(1)
