# 124. Conjuntos - Parte 4

import re

# [a-zA-Z] Retorna uma correspondência para qualquer caractere alfabeticamente entre a e z, minusculas OU maiúsculas

txt = "8 Vezes Antes das 11h45"
x = re.findall("[a-zA-Z]", txt)

print(x)

# [+] Em conjunto, +, *, ., |, (), $, {} Não tem nenhum significado especial, então [+] siginifica: retorna uma correspondência para qualquer caractere + na string

txt = "8 Vezes Antes das + 11h45"
x = re.findall("[+]", txt)
print(x)