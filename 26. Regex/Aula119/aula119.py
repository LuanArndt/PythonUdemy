# 124. Conjuntos - Parte 2

import re

# [^arm] Retorna uma correspondência para qualquer caractere EXCETO 'a', 'r' ou 'm'

txt = "O calor do motor da moto"

x = re.findall("[^arm]", txt)
print(x)

# [0123] Retorna uma correspondência onde qualquer um dos dígitos especificados (0, 1, 2, ou 3) estão presentes

txt = "O calor do motor da minha 12ª moto"

x = re.findall("[0123]", txt)
print(x)