# 124. Conjuntos - Parte 3

import re

# [0-9] Retorna uma correspondencia para qualquer dígito entre 0 e 9

txt = "8 vezes antes das 11h45"

x = re.findall("[0-9]", txt)
print(x)

# [0-5][0-9] Retorna uma correspondência para qualquer número de dois digitos de 00 e 59

x = re.findall("[0-5][0-9]", txt)
print(x)