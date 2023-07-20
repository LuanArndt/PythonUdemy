# 166. Introdução aos widgets tematicos do Tk

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

# Label classica
# criando com variavel
#lbl = tk.Label(root, text="Label classico")
#lbl.pack()

# Criando direto no modulo
tk.Label(root, text="Label Classica").pack()

# Label tematico (ttk)
ttk.Label(root, text="Label Temática").pack()

# No caso da label, não tem diferença visivel

# Ja no botão, conseguimos ver a diferença
# Widget de botao classico
tk.Button(root, text="Label Classica").pack()

# Widget de botao tematico
ttk.Button(root, text="Label Temática").pack()

root.mainloop()