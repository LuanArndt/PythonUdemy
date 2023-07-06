# 117. Metacaracteres - Parte 3

import re

# + Uma ou mais ocorrências "orx+"

txt = "O calor do motor da moto"
x = re.findall("orx+", txt)
print(x)

# Exatamente o número especificado de ocorrencias "al{2}"

txt = "O calor do motor da moto"
# Verifique se a string contém "m" seguido exatamente por dois caracteres "o":
x = re.findall("mo{2}", txt)
print(x)

# | Ou "cai|permanece"
txt = "A chuva na Espanha cai principalmente na planíce!"
x = re.findall("cai|permanece", txt)
print(x)