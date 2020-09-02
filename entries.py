import sqlite3
import datetime


dbpath = 'ledger.db'
# entries(
#                 entry_id INTEGER PRIMARY KEY, 
#                 type_id INTEGER, 
#                 user_id INTEGER, 
#                 target_id INTEGER, 
#                 points FLOAT, 
#                 entryDT TIMESTAMP, 
#                 entryMSG TEXT,
#                 proof TEXT UNIQUE,
#                 FOREIGN KEY (type_id) REFERENCES entryTypes(type_id),
#                 FOREIGN KEY (user_id) REFERENCES users(user_id),
#                 FOREIGN KEY (target_id) REFERENCES targets(target_id)
#                 )

def add(ne):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    command = "INSERT INTO entries VALUES (NULL, {}, {}, {}, {}, '{}', '{}', '{}')".format(ne.type_id, ne.user_id, ne.target_id, ne.points, datetime.datetime.now(), ne.msg, ne.proof)
    #print(command)
    c.execute(command)
    conn.commit()
    conn.close()

def getAll():
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    command = "SELECT * FROM entries"
    ret = c.execute(command).fetchall()
    conn.close()
    return ret

def entriesToPrint(orderby):
    comd = "SELECT user, target, entryMSG, proof, entryDT FROM entries LEFT JOIN users USING (user_id) LEFT JOIN targets USING (target_id) ORDER BY {} DESC".format(orderby)
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute(comd).fetchall()
    conn.close()
    header = ["HUNTER", "TARGET", "MESSAGE", "PROOF", "DATE"]
    first = tuple(header)
    ret.insert(0, first)
    return ret