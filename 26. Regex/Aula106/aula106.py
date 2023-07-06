# 112. A função search()

import re

txt = "O calor do motor da moto"

x = re.search("\s", txt)

print("O primeiro espaço em branco esta na posição:", x.start())

x = re.search("Portugual", txt)
print(x)
