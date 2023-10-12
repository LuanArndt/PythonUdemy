# 208. Caixa de seleção Tkinter

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

concordar = tk.StringVar()

def resultadocheck():
    showinfo("Resultado", f"O usuario {concordar.get()}!")

ttk.Checkbutton(
    root,
    text="Eu concordo",
    variable=concordar,
    command=resultadocheck,
    onvalue="concorda",
    offvalue="não concorda"
).pack()

root.mainloop()