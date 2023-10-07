# 184. Introdução ao widget do botão Tkinter

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

def executar():
    root.quit()

btn1 = ttk.Button(
    root,
    text="Sair",
    command=executar
)

btn1.pack()

root.mainloop()