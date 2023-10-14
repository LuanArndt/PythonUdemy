# 223. Notebook Tkinter

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+350")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(
    notebook,
    width=400,
    height=280,
)

frame2 = ttk.Frame(
    notebook,
    width=400,
    height=280,
)

frame1.pack(fill='both',expand=True)
frame2.pack(fill='both',expand=True)

label1 = ttk.Label(frame1, text="Label - Frame 1", font="Arial 24")
label1.pack()

label2 = ttk.Label(frame2, text="Label - Frame 2", font="Arial 24")
label2.pack()

notebook.add(frame1, text="Informação Geral")
notebook.add(frame2, text="Profile")

root.mainloop()