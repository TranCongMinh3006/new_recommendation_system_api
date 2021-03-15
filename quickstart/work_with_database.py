import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123456",
  database="vnexpress",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  id = x[0]
  user_name = str(id)
  password = str(id)
  name = x[3]
  sql = 'INSERT INTO auth_user (id, password, username,first_name,is_superuser,last_name,email,is_staff,is_active,date_joined) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
  val = (x[0], user_name,password,name,False,"last_name","email",True,True,datetime.now())
  mycursor.execute(sql, val)
  mydb.commit()
  print(val)

#  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#   val =x
#   mycursor.executemany(sql, val)

#   mydb.commit()

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
# ('Peter', 'Lowstreet 4'),
# ('Amy', 'Apple st 652'),
# ('Hannah', 'Mountain 21'),
# ('Michael', 'Valley 345'),
# ('Sandy', 'Ocean blvd 2'),
# ('Betty', 'Green Grass 1'),
# ('Richard', 'Sky st 331'),
# ('Susan', 'One way 98'),
# ('Vicky', 'Yellow Garden 2'),
# ('Ben', 'Park Lane 38'),
# ('William', 'Central st 954'),
# ('Chuck', 'Main Road 989'),
# ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)