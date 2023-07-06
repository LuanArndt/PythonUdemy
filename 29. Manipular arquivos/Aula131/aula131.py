# 137. Métodos para leitura de arquivos

f = open("C:\Python\\29. Manipular arquivos\Aula131\demofile.txt", "r", encoding="UTF-8")
#print(f.readline())
#print(f.readline())

for x in f:
    print(x)

f.close
