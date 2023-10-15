# 230. Usando Tkinter Treeview para exibir dados hierárquicos

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry('400x200')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

tree = ttk.Treeview(
    root,
    columns=('text'),
    show='tree headings'
)
tree.heading('text', text="Departamentos", anchor=tk.W)

# Adicionar dados
tree.insert('', tk.END, values=('Administração'), iid=0, open=False)
tree.insert('', tk.END, values=('Logistica'), iid=1, open=False)
tree.insert('', tk.END, values=('Vendas'), iid=2, open=True)
tree.insert('', tk.END, values=('Financeiro'), iid=3, open=False)
tree.insert('', tk.END, values=('TI'), iid=4, open=False)

# Adicionar dados filhos
tree.insert(0, tk.END, values=('Gabriel'), iid=5, open=False)
tree.insert(2, tk.END, values=('Danny'), iid=6, open=False)
tree.insert(6, tk.END, values=('Arthur'), iid=7, open=False)

tree.grid(column=0, row=0, sticky=tk.NSEW)

root.mainloop()