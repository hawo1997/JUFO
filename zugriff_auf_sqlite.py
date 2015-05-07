import sqlite3 as lite

def Auslesen(Nr,Name):
    con = lite.connect('JUFO.db')
    with con:

        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM %s" % (Name))

        rows = cur.fetchall()
        for row in rows:
            if Nr==row["Raumnr"]:
                return(row["Oeffnungszeiten"])
#            print(row["Raumnr"],row["Raumname"], row["Oeffnungszeiten"])

print(Auslesen(1,"rasp1"))
