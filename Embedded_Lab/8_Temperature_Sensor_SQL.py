import board
import adafruit_dht
import mysql.connector
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
mydb = mysql.connector.connect(
    host="localhost",
    user="testUser",
    password="testPassword",
    database="testDB"
)
print(mydb)
mycursor = mydb.cursor()
sql_query = "INSERT INTO DATA (temp_c, temp_f, humidity) VALUES (%s, %s, %s)"
value = (dhtDevice.temperature, dhtDevice.temperature * 9 / 5 + 32, dhtDevice.humidity)
mycursor.execute(sql_query, value)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
