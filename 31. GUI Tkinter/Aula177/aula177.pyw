# 183. Underline e cursor no label

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

label1 = ttk.Label(
    root,
    text="Label 1",
    font=("Arial", 24),
    underline=1 # Colocar o underline no caracter de indice 1
)

label2 = ttk.Label(
    root,
    text="Label 1",
    font=("Arial", 24, "underline"),
    cursor="hand2"
)

label1.pack()

label2.pack()

root.mainloop()