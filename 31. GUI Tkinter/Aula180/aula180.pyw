# 186. Exibindo um botão de imagem

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

def download_clicked():
    showinfo(
        title="Informação",
        message="Botão de download clicado"
    )

btnIcon = tk.PhotoImage(file="imagens/download.png")

btn1 = ttk.Button(
    root,
    image=btnIcon,
    command=download_clicked
)

btn1.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()