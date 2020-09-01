import sqlite3
from entry import Entry
import operations.targets as targets

# leaderboard(user_id, score, FOREIGN KEY (user_id) REFERENCES users(user_id))

dbpath = 'C:\\Users\\Shyam\\Documents\\GitHub\\Bounty-Ledger-DB-Bot\\ledger.db'


def addRow(user_id):
    ncols = len(targets.getAllTargets())
    command = "INSERT INTO leaderboard VALUES ({}, 0".format(user_id)
    for i in range(1, ncols):
        command = command + ", 0"
    command = command + ")"
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    conn.close()

def addCol(name):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("ALTER TABLE leaderboard ADD COLUMN {} INTEGER".format(name))
    conn.commit()
    c.execute("UPDATE leaderboard SET {}=0".format(name))

def getAll():
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM leaderboard").fetchall()
    conn.close()
    return ret

def getCount(user_id, target):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT {} FROM leaderboard WHERE user_id={}".format(target, user_id)).fetchall()
    conn.close()
    return ret[0][0]

def getScore(user_id):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT score FROM leaderboard WHERE user_id={}".format(user_id)).fetchall()
    conn.close()
    return ret[0][0]

def update(ne):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    if ne.type_id == 1:
        c.execute("UPDATE leaderboard SET {}={} WHERE user_id={}".format(ne.target, getCount(ne.user_id, ne.target)+1, ne.user_id))
        c.execute("UPDATE leaderboard SET score={} WHERE user_id={}".format(getScore(ne.user_id)+ne.points, ne.user_id))
        conn.commit()
    elif ne.type_id == 2:
        c.execute("UPDATE leaderboard SET score={} WHERE user_id={}".format(getScore(ne.user_id)+ne.points, ne.user_id))
        conn.commit()
    conn.close()
    return
