import sqlite3
import datetime
import bountyboard

# users(user_id INTEGER PRIMARY KEY, user TEXT, ign TEXT, join_date TEXT)

dbpath = 'C:\\Users\\Shyam\\Documents\\GitHub\\Bounty-Ledger-DB-Bot\\ledger.db'

def put(user, ign):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (NULL, '{}', '{}', '{}')".format(user, ign, datetime.datetime.now()))
    conn.commit()
    conn.close()
    bountyboard.addRow(getID(user))

def remove(user):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE user='{}' OR ign='{}'".format(user, user)).fetchall()
    conn.commit()
    conn.close()

def getUser(name):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM users WHERE user='{}'".format(name)).fetchall()
    conn.close()
    return ret[0]

def getAllUsers():
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM users").fetchall()
    conn.close()
    return ret

def getID(name):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT user_id FROM users WHERE user='{}' OR ign='{}'".format(name, name)).fetchall()
    conn.close()
    return ret[0][0]
