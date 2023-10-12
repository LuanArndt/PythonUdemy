# 209. Radio Button Tkinter

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

selected_size = tk.StringVar()

def check_size():
    showinfo("Tamanho escolido", f"O tamanho escolido pelo usuario é {selected_size.get()}")

ttk.Label(
    root,
    text="Qual o tamanho da camiseta?"
).pack(fill='x', padx=5, pady=5)

ttk.Radiobutton(
    root,
    text="Pequena",
    value="P",
    variable=selected_size,
    command=check_size
).pack(fill='x', padx=5, pady=5)

ttk.Radiobutton(
    root,
    text="Medio",
    value="M",
    variable=selected_size,
    command=check_size
).pack(fill='x', padx=5, pady=5)

ttk.Radiobutton(
    root,
    text="Grande",
    value="G",
    variable=selected_size,
    command=check_size
).pack(fill='x', padx=5, pady=5)

root.mainloop()