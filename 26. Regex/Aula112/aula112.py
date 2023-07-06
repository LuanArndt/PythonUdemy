# 117. Metacaracteres - Parte 2

import re

txt = "Ola mundo"

# ^ Começa com "^Ola"
x = re.findall("^Ola", txt)
print(x)

# $ Acaba/termina com "mundo$"
x = re.findall("mundo$", txt)
print(x)

# * Zero ou mais ocorrencias "orx*"
txt = "O calor do motor da moto"

#Verifique se a string contém "or" seguido por 0 ou mais caracteres "x":
x = re.findall("orx*", txt)
print(x)