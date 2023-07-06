x = "Ola mundo"
try:
    print(x)
except NameError:
    print("Variavel x não definida")
except:
    print("Aconteceu uma exceção")
else:
    print("Tudo certo por aqui")

print("Continuando o programa")