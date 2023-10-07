# 182. Implicações de largura, altura e quebra de linhas no Label

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

label1 = ttk.Label(
    root,
    text="0123456789",
    font=("Arial", 24),
    borderwidth=1,
    relief="solid",
    #width=5,
    wraplength=120
)

label2 = tk.Label(
    root,
    text="0123456789\n0123456789\n0123456789",
    font=("Arial", 24),
    borderwidth=1,
    relief="solid",
    width=5,
    height=3,
    wraplength=120
)

label1.pack()
label2.pack()
root.mainloop()