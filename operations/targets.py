import sqlite3
from operations import bountyboard
# targets(target_id INTEGER PRIMARY KEY, target TEXT, bounty_amt FLOAT, kill_count INTEGER)




dbpath = 'C:\\Users\\Shyam\\Documents\\GitHub\\Bounty-Ledger-DB-Bot\\ledger.db'

def put(name, BV):    #add new target and their bounty value (float) | return true/false success
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("INSERT INTO targets VALUES (NULL, '{}', {}, 0)".format(name, BV))
    conn.commit()
    conn.close()
    bountyboard.addCol(name)


def remove(name):     # remove target | return true/false success
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("DELETE FROM targets WHERE target='{}'".format(name))
    conn.commit()
    conn.close()

def getAllTargets():  #List of target entries | return List of Lists
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM targets").fetchall()
    conn.close()
    return ret

def getTargetList():
    ret = []
    targs = getAllTargets()
    targs = targs[1:]
    for i in getAllTargets():
        ret.append(i[1])
    return ret

def getTarget(name):  #get target entry | return List
    #print(name)
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM targets WHERE target='{}'".format(name)).fetchall()
    conn.close()
    return ret[0]

def incrKC(name):   #increase kill_count for specified target by 1 | return true/false success
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    currKC = c.execute("SELECT kill_count FROM targets WHERE target='{}'".format(name)).fetchall()[0][0]
    c.execute("UPDATE targets SET kill_count={} WHERE target='{}'".format((currKC+1),name))
    conn.commit()
    conn.close()

def getID(name):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT target_id FROM targets WHERE target='{}'".format(name)).fetchall()
    conn.close()
    return ret[0][0]

def getBounty(name):
    return getTarget(name)[2]

def changeBounty(name, BV):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("UPDATE targets SET bounty_amt={} WHERE target='{}'".format(BV,name))
    conn.commit()
    conn.close()


# conn = sqlite3.connect(dbpath)
# c = conn.cursor()
# ret = c.execute("SELECT * FROM targets").fetchall()
# print(ret)
# incrKC("Adam")
# print(getTarget("Adam"))
# conn.close()

"""
conn = sqlite3.connect(dbpath)
c = conn.cursor()
ret = c.execute("SELECT * FROM targets").fetchall()
conn.close()


c.execute("INSERT INTO targets VALUES (NULL, 'Adam', 10.0, 0)")
c.execute("INSERT INTO targets VALUES (NULL, '6th', 6.0, 0)")
c.execute("INSERT INTO targets VALUES (NULL, 'enerd', 3, 0)")
c.execute("INSERT INTO targets VALUES (NULL, 'redscout', 3, 0)")
conn.commit()
"""


