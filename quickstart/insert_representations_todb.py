import mysql.connector
from datetime import datetime
import requests
import json

data = requests.get('http://localhost:9000/NPA/user_vector')
data = data.json()

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123456",
  database="vnexpressdemo",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM users")

for x in data['data']:
  userId = int(x['userID'])
  representation = str(x['representation'])
  sql = 'INSERT INTO users(userId,representation) values(%s,%s)'
  val = (userId, representation)
  mycursor.execute(sql, val)
  mydb.commit()
  print(val)