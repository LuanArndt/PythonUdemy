# 218. Tkinter Sizegrip

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")
root.resizable(True, True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sg = ttk.Sizegrip(root)

sg.grid(
    row=1,
    sticky=tk.SE,
    
)

root.mainloop()