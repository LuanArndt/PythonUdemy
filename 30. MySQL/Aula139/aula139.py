# 145. Chave primária

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Criar a tabela ja com o campo da chave primaria:
#sql = """
#    CREATE TABLE pessoas (
#            id INT AUTO_INCREMENT PRIMARY KEY
#            nome VARCHAR(255), 
#            idade INT(2)
#"""

# Adicionar o campo de chave primaria em uma tabela que ja existe:
sql = """
    ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST
"""

mycursor.execute(sql)

