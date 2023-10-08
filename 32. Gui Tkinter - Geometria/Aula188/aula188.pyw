# 194. Usando a opção de expansão

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de geometria")
root.geometry("600x400+650+300")

# box 1 
box1 = tk.Label(
    root,
    text="Box 1",
    bg="green",
    fg="white"
)

box1.pack(
    ipadx=10,
    ipady=10,
    fill="both", # x, y, both
    expand=True
)

# box 2

box2 = tk.Label(
    root,
    text="Box 2",
    bg="red",
    fg="white"
)

box2.pack(
    ipadx=10,
    ipady=10,
    fill="both",
    expand=True
)

root.mainloop()