# 190. StringVar e textvariable no widget Tkinter Entry

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

# Armazena os valores do textbox

texto = tk.StringVar()
texto.set("Insira seu nome...")

textbox = ttk.Entry(
    root,
    textvariable=texto,
    font="Arial 24 italic"
)

textbox.focus()
textbox.select_range(0,tk.END)

btn1 = ttk.Button(
    root,
    text="Executar",
    command=lambda: print(texto.get())
)

textbox.pack()
btn1.pack()

root.mainloop()