# 216. Tkinter Spinbox

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

current_value = tk.StringVar(value=0)

def value_changed():
    print(current_value.get())

spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=10,
    font="Arial 24",
    textvariable=current_value,
    command=value_changed,
    wrap=True
)


spin_box.pack()

root.mainloop()