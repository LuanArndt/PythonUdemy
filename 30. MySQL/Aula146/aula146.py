# 152. Atualizar registros da tabela

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE pessoas SET idade = %s WHERE nome = %s"
val = ('26', 'Luan')

mycursor.execute(sql, val)
mydb.commit()