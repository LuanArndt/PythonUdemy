# 133. Executando o bloco finaly

x = "Ola mundo"
# Try = Tenta executar
try:
    print(x)

# except = Se der erro no try, executa algum except
except NameError:
    print("Variavel x não definida")
except:
    print("Aconteceu uma exceção")

# else = É executado somente se o try executar com sucesso
else:
    print("Tudo certo por aqui")

# finally = É executado em qualquer hipotese. Se o try der erro ou não
finally:
    print("O try except foi finalizado")

print("Continuando o programa")