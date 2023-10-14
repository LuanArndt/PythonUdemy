# 227. Definir barra de rolagem para o Treeview

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

# Gerar dados de exemplo
contacts = []
for n in range(1,100):
    contacts.append((f'nome {n}', f'sobrenome {n}', f'email{n}@exemplo.com'))

# Adicionar dados na tabela
for contact in contacts:
    tree.insert('', tk.END, values=contact)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)

tree.bind("<<TreeviewSelect>>", item_selected)

tree.grid(row=0, column=0, sticky=tk.NSEW)

# Adicionar barra de rolagem
scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=tree.yview
)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

root.mainloop()