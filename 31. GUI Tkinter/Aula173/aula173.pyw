# 179. Definir uma fonte específica para o Label

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

label1 = ttk.Label(
    root, 
    text="Esse é um label",
    #font="Times 24 bold italic"
    font=("Verdana", 24, "bold")
)

label1.pack()
root.mainloop()