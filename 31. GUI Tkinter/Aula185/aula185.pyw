# 191. Manipular eventos do widget Entry

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

def btn1_clicked(event=None):
    if texto.get() != "Insira seu nome...":
        msg = f"Bem vindo(a) {texto.get()}!"
        showinfo(title="Informação", message=msg)
        texto.set("Insira seu nome...")
        textbox.focus()
        textbox.select_range(0,tk.END)

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
textbox.bind("<Return>", btn1_clicked)
textbox.pack()

btn1 = ttk.Button(
    root,
    text="Executar",
    command=btn1_clicked
)

btn1.pack()

root.mainloop()