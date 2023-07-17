# 153. Limite o resultado

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Limitar apenas o retorno de 2 registros:
#sql = "SELECT * FROM pessoas LIMIT 2"

# Limita para 2 retornos, mas começando pelo segundo registro
sql = "SELECT * FROM pessoas LIMIT 2 OFFSET 2"

mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
