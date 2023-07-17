# 154. Juntar registros de duas tabelas

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Junta as tabelas e ignora o que não tem relação
#sql = """
#SELECT
#    usuarios.nome AS nome, produtos.nome AS favorito
#    FROM usuarios
#    INNER JOIN produtos ON usuarios.fav = produtos.id
#"""

# Junta as tabelas e mostra o resultado mesmo se não tiver relação
sql = """
SELECT
    usuarios.nome AS nome, produtos.nome AS favorito
    FROM usuarios
    LEFT JOIN produtos ON usuarios.fav = produtos.id
"""

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
