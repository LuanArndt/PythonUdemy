# 168. Introdução à vinculação de comandos no Tkinter

import tkinter as tk
from tkinter import ttk

def button_clicked():
    root.config(background="gray")
    print("Botão clicado")

root = tk.Tk()

root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

btn = ttk.Button(root, text="Clique me", command=button_clicked)
btn.pack()

root.mainloop()