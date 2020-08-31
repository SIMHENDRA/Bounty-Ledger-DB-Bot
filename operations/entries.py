import sqlite3
import datetime
import entry

dbpath = 'C:\\Users\\Shyam\\Documents\\GitHub\\Bounty-Ledger-DB-Bot\\data\\ledger.db'
# entries(
#                 entry_id INTEGER PRIMARY KEY, 
#                 type_id INTEGER, 
#                 user_id INTEGER, 
#                 target_id INTEGER, 
#                 points FLOAT, 
#                 entryDT TIMESTAMP, 
#                 entryMSG TEXT, 

#                 FOREIGN KEY (type_id) REFERENCES entryTypes(type_id),
#                 FOREIGN KEY (user_id) REFERENCES users(user_id),
#                 FOREIGN KEY (target_id) REFERENCES targets(target_id)
#                 )

def handleEntry(ne):
    add(ne)
    updLB(ne)

def add(ne):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    command = "INSERT INTO entries VALUE (NULL, {}, {}, {}, {}, '{}', '{}')".format(ne.type_id, ne.user_id, ne.target_id, ne.points, datetime.datetime.now(), ne.msg)
    c.execute(command)
    c.commit()
    conn.close()

def updLB(ne):
    pass

