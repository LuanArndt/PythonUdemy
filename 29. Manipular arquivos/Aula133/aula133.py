# 139. Excluir arquivos

# As proximas 3 linhas não fazem parte da aula. Servem apenas para o ptyhon determinar onde está o .py atual e mudar o "workdir" para la.
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
## Aula:

# Para evitar erro de arquivo inexistente
# Metodo 1 - try:
try:
    os.remove("demofile.txt")
except FileNotFoundError:
    print("O arquivo não existe")

# Metodo 2 - if:
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("Não existe")

# Remover pasta:
os.rmdir("TesteDir")