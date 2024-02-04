import Adafruit_DHT
from time import sleep
import sqlite3

try:
    sqliteConnection = sqlite3.connect('blackberry_dht.db')
    cursor = sqliteConnection.cursor()

    cursor.execute('SELECT * FROM dht')
    entries = cursor.fetchone()
    print(entries)
    if entries == None:
        print("CREATE TABLE ENTRIES")
        cursor.execute('INSERT INTO dht (id,temp,humidity) VALUES(1,0,0);')
        sqliteConnection.commit()
except:
    print("SQL error")

dht = Adafruit_DHT.DHT11

while True:
    humidity, temp = Adafruit_DHT.read(dht, 4)
    try:
        cursor.execute('UPDATE dht SET temp=?, humidity=? WHERE id=1',(temp, humidity))
        sqliteConnection.commit()
    except:
        print("Error updating SQL table")
    sleep(2)
else:
    cursor.close()
    if sqliteConnection:
        sqliteConnection.close()


