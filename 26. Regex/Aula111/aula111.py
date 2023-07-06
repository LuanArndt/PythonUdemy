# 117. Metacaracteres - Parte 1

import re

# [] Um conjunto de caracteres "[a-m]"
txt = "O calor do motor da moto"

# Encontre todos os caracteres minúsculos em ordem alfabetica entre "a" e "m":

x = re.findall("[a-m]", txt)
print(x)

# \ Sinaliza uma sequência especial (também pode ser usada para caracteres de escape) "\d"
txt = "Eu tenho 36 anos de idade"

# Procurar caracteres de digito "\d"
x = re.findall("\d", txt)
print(x)

# . Qualquer caractere (exceto caractere de nova linha) "mu.o"

# Procure uma sequência que comece com "mu", seguido por dois (qualquer) caracteres e um "o":
txt = "Ola mundo"
x = re.findall("mu..o", txt)
print(x)