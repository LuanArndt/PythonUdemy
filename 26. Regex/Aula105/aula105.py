# 111. Regex em Python

# Importar modulo do regex
import re

txt = "O Gabriel é amigo do Miguel"

x = re.search("^O.*Miguel$", txt)
if x:
    print("Sim")
else:
    print("Não")