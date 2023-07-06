# 124. Conjuntos - Parte 1

import re

# [arm] Retorna uma correspondência onde um dos caracteres especificados (a, r ou m) está presente

txt = "O calor do motor da moto"

x = re.findall("[arm]", txt)
print(x)

# [a-m] retorna uma correspondência para qualquer caractere minúsculo, em ordem alfabética entre 'a' e 'm'

x = re.findall("[a-m]", txt)
print(x)