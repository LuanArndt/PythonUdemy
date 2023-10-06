# 172. Registrar vários manipuladores para o mesmo evento

import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Tecla entre pressionada")

def log(event):
    print(event)

root = tk.Tk()

root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

btn1 = ttk.Button(root, text="Executar")
# O metodo de return, é chamado quando a tecla enter é precionada.
btn1.bind("<Return>", return_pressed) 
# Abaixo, está sendo adicionado uma nova bind ao botão. Se o "add="+"" não for usado, ele vai apenas substituir
btn1.bind("<Return>", log, add="+")
btn1.focus()
btn1.pack(expand=True)

root.mainloop()