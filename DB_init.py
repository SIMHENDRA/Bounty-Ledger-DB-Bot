import sqlite3
import datetime                                                   

def initDB():
    conn = sqlite3.connect('ledger.db')
    c = conn.cursor()

    c.execute("CREATE TABLE users(user_id INTEGER PRIMARY KEY, user TEXT UNIQUE, ign TEXT, join_date TIMESTAMP)")
    c.execute("CREATE TABLE targets(target_id INTEGER PRIMARY KEY, target TEXT UNIQUE, bounty_amt FLOAT, kill_count INTEGER)")
    c.execute("CREATE TABLE entryTypes(type_id INTEGER PRIMARY KEY, desc TEXT UNIQUE)")
    c.execute("""CREATE TABLE entries(
                    entry_id INTEGER PRIMARY KEY, 
                    type_id INTEGER, 
                    user_id INTEGER, 
                    target_id INTEGER, 
                    points FLOAT, 
                    entryDT TIMESTAMP, 
                    entryMSG TEXT,
                    proof TEXT UNIQUE, 
                    FOREIGN KEY (type_id) REFERENCES entryTypes(type_id),
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (target_id) REFERENCES targets(target_id)
                    )""")
    c.execute("CREATE TABLE leaderboard(user_id, score, FOREIGN KEY (user_id) REFERENCES users(user_id))")
    c.execute("INSERT INTO targets VALUES (NULL, 'dummy', 0.0, 0)")

    conn.commit()
    conn.close()
    return