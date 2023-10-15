# 228. Excluir item do Treeview

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+350")

# Definir as colunas
columns = ('nome', 'sobrenome', 'email')
tree = ttk.Treeview(
    root,
    columns=columns,
    show='headings'
)

# Definir cabeçalhos
tree.heading('nome', text='Nome')
tree.heading('sobrenome', text='Sobrenome')
tree.heading('email', text="Email")

# Adicionar dados na tabela
tree.insert("", tk.END, values=('Gabriel', 'Artigas', 'gabriel@email.com'))
tree.insert('', tk.END, values=('Danny', 'Maciel', 'danny@email.com'))
tree.insert('', tk.END, values=('Arthur', 'Maciel', 'arthur@email.com'))
tree.insert('', tk.END, values=('Beatriz', 'Silva', 'bia@email.com'))
tree.insert('', tk.END, values=('Lucas', 'Silva', 'lucas@email.com'))

def item_selected(event):
    for selected_item in tree.selection():
        tree.delete(selected_item)

tree.bind("<<TreeviewSelect>>", item_selected)

tree.grid(row=0, column=0, sticky=tk.NSEW)

root.mainloop()