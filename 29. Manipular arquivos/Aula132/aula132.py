# 138. Gravação de arquivos

# As proximas 3 linhas não fazem parte da aula. Servem apenas para o ptyhon determinar onde está o .py atual e mudar o "workdir" para la.
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
## Aula:

# Metodo "x": Cria um arquivo. Se ja existir, da erro
f = open("demofile.txt", "x")

# Metodo "a": se o arquivo não existir, cria. Se ja existir, adiciona novo conteudo
f = open("demofile.txt", "a")
f.write("Agora o arquivo tem conteudo\n")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

# Metodo "w": Sobescreve o conteudo

f = open("demofile.txt", "w")
f.write("Conteudo sobescrito\n")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()