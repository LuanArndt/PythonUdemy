# 114. A função split()

import re
txt = "O calor do motor da moto"

# Divide a string pelos expaços, gerando uma lista onde cada palavra é um item
x = re.split("\s", txt)
print(x)

# Divide apenas nas 2 primeiras ocorrencias do espaço
x = re.split("\s", txt, 2)
print(x)