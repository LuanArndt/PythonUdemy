# 141. Criar conexão com servidor MySQL

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!"
)

print(mydb)