import sqlite3
import datetime


dbpath = 'ledger.db'

def put(description):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("INSERT INTO entryTypes VALUES (NULL, '{}')".format(description))
    conn.commit()
    conn.close()

def getID(description):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT type_id FROM entryTypes WHERE desc='{}'".format(description)).fetchall()
    conn.close()
    return ret[0][0]

