import sqlite3
import datetime

ht_db = '/var/jail/home/porderiq/lab06/lab06b.db'
now = datetime.datetime.now()

def request_handler(request):
    if request["method"]=="POST":
        user = request['form']['user']
        temp = request['form']['temp']
        pressure = request['form']['pressure']

        with sqlite3.connect(ht_db) as c:
            c.execute("""CREATE TABLE IF NOT EXISTS sensor_data (time_ timestamp, user text, temperature real, pressure real);""")
            c.execute('''INSERT into sensor_data VALUES (?,?,?,?);''', (now, user, temp, pressure))

        return "Data POSTED successfully"
    else:
        return "invalid HTTP method for this url."
