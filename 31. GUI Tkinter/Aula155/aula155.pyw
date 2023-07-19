# 161. Comportamento de redimensionamento

import tkinter as tk
root = tk.Tk()
root.title("Noite feliz")
root.geometry("200x200+100-100")

# Por padrão, o resizable fica true para X e Y, permitindo o redimencioamento tanto de altura, quanto de largura da janela:
#root.resizable(True, True)

# Dessa forma, não posso mais redimencionar:
#root.resizable(False, False)

# Definir tamanho minimo e maximo para a janela:
root.minsize(100, 100)
root.maxsize(300,300)

root.mainloop()