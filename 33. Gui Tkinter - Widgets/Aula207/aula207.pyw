# 213. Adicionando uma barra de rolagem à caixa de listagem

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'Javascript', 'PHP', 'Swift')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    font="Arial, 24",
    selectmode="extended" # browse ou extended
)

listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)

scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
    command=listbox.yview
)

scrollbar.grid(
    column=1,
    row=0,
    sticky='ns'
)

listbox['yscrollcommand'] = scrollbar.set

def items_selected(event):
    selected_indices = listbox.curselection()
    for i in selected_indices:
        print(listbox.get(i))

listbox.bind("<<ListboxSelect>>", items_selected)

root.mainloop()