# 176. Desvinculação de eventos

import tkinter as tk
from tkinter import ttk

def log(event):
    print("Evento disparado...")

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")

btn1 = tk.Button(root, text="Executar 1")
# Vincula o evento:
btn1.bind("<Return>", log)
btn1.focus()
btn1.pack()

# Desvincula o evento:
btn2 = ttk.Button(
    root,
    text="Desvincular evento de executar",
    command=lambda: btn1.unbind("<Return>")
)

btn2.pack()

btn3 = ttk.Button(
    root,
    text="Vincular evento de executar",
    command=lambda: btn1.bind("<Return>",log)
)

btn3.pack()

root.mainloop()