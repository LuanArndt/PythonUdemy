# 134. Levantar/Lançar uma exceção

x = 1

if x < 0:
    raise Exception("Não são permitidos números negativos")

y = "Ola mundo!"

if not type(y) is int:
    raise TypeError("Somente números")

print("Fim do programa")