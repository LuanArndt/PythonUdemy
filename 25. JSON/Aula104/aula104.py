# 110. Formatar resultado JSON
import json

x = {
    "nome": "Gabriel",
    "idade": 36,
    "casado": True,
    "divorciado": False,
    "filhos": ("Arthur","Lucas"),
    "pets": None,
    "carros": [
        {"modelo": "BMW 230", "cor": "Branca"},
        {"modelo": "Ford Edge", "cor": "Preto"}
    ]
}
#Sem indentação:
print("---")
print(json.dumps(x))
      
#Com indentação:
print("---")
print(json.dumps(x, indent=2))

#Alterando o separador
print("---")
print(json.dumps(x, indent=2, separators=(",", " = ")))

#Ordenando
print("---")
print(json.dumps(x, indent=2, separators=(",", " = "), sort_keys=True))
