# 220. Tkinter Progressbar

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

pb = ttk.Progressbar(
    root,
    orient=tk.HORIZONTAL,
    length=300,
    mode="indeterminate"
)

pb.pack()

pb.start(10)

root.mainloop()