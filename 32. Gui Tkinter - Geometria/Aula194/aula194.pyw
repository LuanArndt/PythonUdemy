# 200. Introdução ao gerenciador de geometria place

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de geometria")
root.geometry("600x400+700+300")

# widget.place(**options)
# label1
label1 = ttk.Label(
    root,
    text="Posição absoluta",
    background="red",
    foreground="white",
    font="Arial 24"
)

label1.place(x=20, y=20)

# label2
label2 = ttk.Label(
    root,
    text="Posição relativa",
    background="blue",
    foreground="white",
    font="Arial 24"
)

label2.place(relx=0.8, rely=0.2, anchor=tk.NE, relwidth=0.5)

root.mainloop()
