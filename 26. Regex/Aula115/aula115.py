# 121. Sequências especiais - Parte 2

import re

# \B Retorna uma correspondência onde os caracteres especificados estão presentees, mas NÃO no início (ou no final) de uma palavra
# (o "r" no inicio está garantindo que a string está sendo tratada com uma "string bruta") r"\Btor", r"tor\B"

txt = "O calor do motor da moto dos pastores torradores"

# Verifique se "tor" está presente, mas NÃO no inicio de uma palavra:
x = re.findall("\Btor", txt)
print(x)


# Verifique se "tor" está presente, mas NÃO no final de uma palavra:
x = re.findall("tor\B", txt)
print(x)

# \d Retorna uma correspondência onde a string contém dígitos (números de 0 a 9) "\d"

txt = "O calor do motor da minha 12ª moto"
x = re.findall("\d", txt)
print(x)

# \D Retorna uma correspondência onde a string NÃO contém dígitos (números de 0 a 9) "\D"

txt = "O calor do motor da moto"
x = re.findall("\D", txt)
print(x)

