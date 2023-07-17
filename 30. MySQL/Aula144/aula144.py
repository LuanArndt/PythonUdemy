# 150.Excluir registros da tabela

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM pessoas WHERE nome = 'Rai'"

mycursor.execute(sql)
mydb.commit()