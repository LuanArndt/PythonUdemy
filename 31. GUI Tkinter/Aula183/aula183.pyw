# 189. Mostrando uma entrada de senha Tkinter

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

textbox = ttk.Entry(
    root,
    show="*"
)

textbox.focus()

btn1 = ttk.Button(
    root,
    text="Executar",
    command=lambda: print(textbox.get())
)

textbox.pack()
btn1.pack()

root.mainloop()