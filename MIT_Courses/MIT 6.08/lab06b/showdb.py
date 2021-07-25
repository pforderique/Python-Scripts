import sqlite3
ht_db = '/var/jail/home/porderiq/lab06/lab06b.db'

with sqlite3.connect(ht_db) as c:
    results = c.execute('''SELECT * FROM sensor_data;''').fetchall()
    print(results) 
