# 212. Vinculando o evento select

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'Javascript')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    font="Arial, 24",
    selectmode="extended" # browse ou extended
)

listbox.pack()

def items_selected(event):
    selected_indices = listbox.curselection()
    for i in selected_indices:
        print(listbox.get(i))

listbox.bind("<<ListboxSelect>>", items_selected)

root.mainloop()