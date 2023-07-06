# 109. Converter de Python para JSON

import json

x = {
    "nome":"Gabriel",
    "idade":36,
    "cidade":"São Paulo"
}

y = json.dumps(x)
print(y)