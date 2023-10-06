# 180. Exibindo uma imagem no Label

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

img1 = tk.PhotoImage(file="imagens\Python.png")
label1 = ttk.Label(
    root,
    image=img1,
    text="Logo Python",
    font=("Arial", 20),
    compound="top" # top, bottom, left, right, none, text, image
)
label1.pack()
root.mainloop()