# 142. Criar base de dados

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

