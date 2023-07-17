# 146. Inserir dados na tabela

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()


#sql = """
#    INSERT INTO pessoas (id, nome, sobrenome, idade) 
#    VALUES (NULL, 'Luan', 'Gabriel Arndt', 25)
#"""

sql = """
    INSERT INTO pessoas (id, nome, sobrenome, idade) 
    VALUES (NULL, %s, %s, %s)
"""
val = [
    ("Janete", "Becker", 52),
    ("Rai", "Gustavo Arndt", 18),
    ("Luan", "Gabriel Arndt", 25),
    ("Tamires", "De Souza", 21)

]
#mycursor.execute(sql, val)

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "registros inseridos")
print(mycursor.lastrowid)