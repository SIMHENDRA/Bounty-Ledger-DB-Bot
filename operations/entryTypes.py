import sqlite3
import datetime



dbpath = 'C:\\Users\\Shyam\\Documents\\GitHub\\Bounty-Ledger-DB-Bot\\data\\ledger.db'

def put(description):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("INSERT INTO entryTypes VALUE (NULL, '{}')".format(description))
    c.commit()
    conn.close()

def getID(description):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT type_id FROM entryTypes WHERE desc='{}'".format(description)).fetchall()
    conn.close()
    return ret[0][0]

