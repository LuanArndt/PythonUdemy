# 206. Tkinter ScrolledText

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title("Python Tkinter")

st = ScrolledText(
    root,
    width=50,
    height=10
)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()