import sqlite3

conn = sqlite3.connect('ledger.db')
c = conn.cursor()
c.execute("ALTER TABLE targets ADD COLUMN tk TEXT")
conn.commit()
c.execute("UPDATE targets SET tk = 'No'")
conn.commit()
conn.close()
