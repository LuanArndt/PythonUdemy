# 115. A função sub()

import re
txt = "O calor do motor da moto"

# Substitui as ocorrencias da string por outra string

# Nesse caso, substitui o espaço pelo underline
x = re.sub("\s", "_", txt)
print(x)

# Substitui apenas as 2 primeiras ocorrencias de espaço
x = re.sub("\s", "_", txt, 2)
print(x)
