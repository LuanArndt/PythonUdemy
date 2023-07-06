# 113. A função findall()

import re

txt = "O calor do motor da moto"
x = re.findall("or", txt)
print(x)


x = re.findall("rola", txt)
print(x)

if x:
    print("Sim,", x)
else:
    print("Não, otario!")