# 157. Extensão .py vs .pyw

# .pyw
# O .pyw não vai depender de um console aberto.
# Por exemplo, se eu colocar meu python para um exe, no .py ele vai abrir um console junto. Ja no .pyw a console ficara em segundo plano.

import tkinter as tk

root = tk.Tk()

root.mainloop()