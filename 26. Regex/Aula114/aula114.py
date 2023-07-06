# 120. Sequências especiais - Parte 1

import re

# \A Retorna uma correspondência se os caracteres especificados estiverem no início da string

txt = "Bem vindo ola ao mundo"
x = re.findall("\AOla", txt)
print(x)

# \b Retorna uma correspondência onde os caracteres especificados estão no início ou no final de uma palavra

# (o "r" no inicio está garantindo que a string está sendo tratada como uma "string bruta") r"\btor", r"tor\b"

txt = "O calor do motor da moto"

# Verifique se "tor" está presente no início de uma PALAVRA

x = re.findall(r"\btor", txt)
print(x)

# Verifique se "tor" está presente no final de uma PALAVRA

x = re.findall(r"tor\b", txt)
print(x)