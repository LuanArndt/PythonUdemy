# 156. Tkinter Olá, mundo!

import tkinter as tk

root = tk.Tk()

lbl = tk.Label(root, text="Ola, mundo!")
lbl.pack()

# O metodo mainloop mantem a janela aberta e por padrão é usada por ultimo no codigo
root.mainloop()



