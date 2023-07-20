# 169. Argumentos de comandos do botão Tkinter

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

def select(arg):
    root.config(background=arg)

btn1 = ttk.Button(
    root, 
    text="Vermelho",
    command=lambda: select("red")
)

btn2 = ttk.Button(
    root, 
    text="Azul",
    command=lambda: select("blue")
)

btn1.pack()
btn2.pack()

root.mainloop()