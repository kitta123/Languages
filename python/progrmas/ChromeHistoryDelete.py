import sqlite3
import re

conn = sqlite3.connect('history path')
c = conn.cursor()

id = 0
result = true

while result:
    result = False
    ids = []
    for rows in c.execute("SELECT id,urls FROM urls Where url LIKE ''%youtube%'"):
        print(rows)
        id = rows[0]
        ids.append((id,))
    c.executemany('DELETE from urls WHERE id=?',ids)
    conn.commit()

conn.close()
