import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
a = cur.execute(f'SELECT number FROM card;')
print(not a.fetchall())
