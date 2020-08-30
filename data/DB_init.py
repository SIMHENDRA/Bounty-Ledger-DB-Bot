import sqlite3

#conn = sqlite3.connect('bounty_hunting.db')
conn = sqlite3.connect('ledger.db')
c = conn.cursor()

c.execute("CREATE TABLE users(user_id INTEGER PRIMARY KEY, user TEXT, ign TEXT, join_date TEXT)")
c.execute("CREATE TABLE targets(target_id INTEGER PRIMARY KEY, target TEXT, bounty_amt FLOAT, kill_count INTEGER)")
c.execute("CREATE TABLE entryTypes(type_id INTEGER PRIMARY KEY, desc TEXT)")
c.execute("""CREATE TABLE entries(
                entry_id INTEGER PRIMARY KEY, 
                type_id INTEGER, 
                user_id INTEGER, 
                target_id INTEGER, 
                points FLOAT, 
                entryDT TEXT, 
                entryMSG TEXT, 
                FOREIGN KEY (type_id) REFERENCES entryTypes(type_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (target_id) REFERENCES targets(target_id)
                )""")

c.execute("INSERT INTO targets VALUES (NULL, 'Adam', 10.0, 0)")
c.execute("INSERT INTO targets VALUES (NULL, '6th', 6.0, 0)")
c.execute("INSERT INTO targets VALUES (NULL, 'enerd', 3, 0)")
c.execute("INSERT INTO targets VALUES (NULL, 'redscout', 3, 0)")
conn.commit()



conn.commit()
conn.close()