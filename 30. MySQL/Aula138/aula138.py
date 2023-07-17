# 144. Alterar a estrutura da tabela

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Criar um novo campo na tabela:
#sql = """
#    ALTER TABLE pessoas ADD sobrenome VARCHAR(255)
#"""

# Remover um campo da tabela
sql = """
    ALTER TABLE pessoas DROP sobrenome
"""
mycursor.execute(sql)

# Cria um novo campo no inicio da tabela:
#sql = """
#    ALTER TABLE pessoas ADD sobrenome VARCHAR(255) FIRST
#"""

# Cria um novo campo depois de um campo especifico
sql = """
    ALTER TABLE pessoas ADD sobrenome VARCHAR(255) AFTER nome
"""

mycursor.execute(sql)

