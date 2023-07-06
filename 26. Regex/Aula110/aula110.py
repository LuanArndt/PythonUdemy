# 116. objeto de correspondência

import re
txt = "O calor do motor da Moto"

x = re.search(r"\bM\w+", txt)
print(x)

print(x.span())
print(x.string)
print(x.group())