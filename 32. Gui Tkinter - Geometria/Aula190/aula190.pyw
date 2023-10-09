# 196. Quando usar o gerenciador de geometria pack

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de geometria")
root.geometry("600x400+650+300")

# Coloque widgets de cima para baixo

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
    fill="x"
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
    fill="x"
)

# box 3

box3 = tk.Label(
    root,
    text="Box 3",
    bg="blue",
    fg="white"
)

box3.pack(
    ipadx=10,
    ipady=10,
    fill="x"
)

# box 4

box4 = tk.Label(
    root,
    text="Esquerda",
    bg="cyan",
    fg="black"
)

box4.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill="both",
    side="left"
)

# box 5

box5 = tk.Label(
    root,
    text="Centro",
    bg="magenta",
    fg="black"
)

box5.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill="both",
    side="left"
)


# box 6

box6 = tk.Label(
    root,
    text="Direita",
    bg="yellow",
    fg="black"
)

box6.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill="both",
    side="left"
)

root.mainloop()