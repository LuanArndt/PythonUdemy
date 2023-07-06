# 108. Analisar JSON - Converter de JSON para Python
import json

#json:
x = '{"nome":"Gabriel", "idade":36, "cidade":"São Paulo"}'

#transforma o json em um dictionary do python:
y = json.loads(x)

print(y)
print(y["nome"])
print(y["idade"])
print(y["cidade"])