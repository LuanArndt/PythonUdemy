# 123. Sequências especiais - Parte 4

import re

# \w Retorna uma correspondencia em que a string contém quaisquer caracteres de palavra (caracteres de 'a' a 'z', dígitos de 0-9 e o caracter sublinhado _) "\w"

txt = "O calor do motor da moto 2022"

x = re.findall("\w", txt)
print(x)

# \W retorna uma correspondencia em que a string NÃO contém nenhum caractere de palavra "\W"

txt = "O calor do motor da moto 2022 _ @"
x = re.findall("\W", txt)
print(x)

# \Z retorna uma correspondencia se os caracteres especificados estiverem no final da string "moto\Z"
txt = "O calor do motor da moto"

x = re.findall("moto\Z", txt)
print(x)
