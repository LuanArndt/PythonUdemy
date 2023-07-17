# 151. Apagar uma tabela

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="adminuser",
    password="adminadmin123!",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Apaga. Se não existir, da erro.
#sql = "DROP TABLE pessoas"

# Apagar somente se existir. Se não, não da erro. 
sql = "DROP TABLE IF EXISTS pessoas"

mycursor.execute(sql)