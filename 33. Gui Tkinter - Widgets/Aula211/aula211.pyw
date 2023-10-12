# 217. Definir etapas discretas no SpinBox

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

current_value = tk.StringVar(value=0)

def value_changed():
    print(current_value.get())

valores = (0, 2, 4, 6 , 8, 10)

spin_box = ttk.Spinbox(
    root,
    font="Arial 24",
    textvariable=current_value,
    command=value_changed,
    wrap=True,
    values=valores
)


spin_box.pack()

root.mainloop()