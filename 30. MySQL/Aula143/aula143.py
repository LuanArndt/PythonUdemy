# 149. Classifique o resultado

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Pegar todos os valores e ordenar por idade:
#sql = "SELECT * FROM pessoas ORDER BY idade"

# Ordenar na ordem decresscente:
sql = "SELECT * FROM pessoas ORDER BY idade DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)