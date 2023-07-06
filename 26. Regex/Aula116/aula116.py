# 122. Sequências especiais - Parte 3

import re

# \s Retorna uma correspondencia onde a string contém um caractere de espaço em branco "\s"

txt = "O calor do motor da moto"

# Retorne uma correspondencia para cada caractere de espaço em branco:
x = re.findall("\s", txt)
print(x)

# \S Retorna uma correspondencia onde a string NÃO contem um caractere de espaço em branco

x = re.findall("\S", txt)
print(x)