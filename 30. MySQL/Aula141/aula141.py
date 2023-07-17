# 147. Selecionar dados de uma tabela

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()
#sql = "SELECT * FROM pessoas"
sql = "SELECT nome, idade FROM pessoas"
mycursor.execute(sql)

# Pegar todos os registros da tabela
#myresult = mycursor.fetchall()
#for x in myresult:
#    print(x)

# Pegar apenas o primeiro registro da tabela
myresult = mycursor.fetchone()
print(myresult)