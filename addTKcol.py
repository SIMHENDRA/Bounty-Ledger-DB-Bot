import sqlite3

conn = sqlite3.connect('ledger.db')
c = conn.cursor()
c.execute("ALTER TABLE targets ADD COLUMN notes TEXT")
conn.commit()
c.execute("UPDATE targets SET tk = 'No tk pts'")
conn.commit()
conn.close()
