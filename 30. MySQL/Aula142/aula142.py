# 148. Selecionar com um filtro

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Pegar todos os registros que contenham 'Arndt' no sobrenome:
#sql = "SELECT * FROM pessoas WHERE sobrenome like '%Arndt%'"

# Outra forma de fazer a mesma coisa:
sql = "SELECT * FROM pessoas WHERE sobrenome LIKE %s"
sobrenome = ("%Arndt%",)

mycursor.execute(sql, sobrenome)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
