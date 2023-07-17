# 143. Criação de uma tabela

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = """CREATE TABLE pessoas (
            nome VARCHAR(255), 
            idade INT(2)
        )"""

mycursor.execute(sql)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)