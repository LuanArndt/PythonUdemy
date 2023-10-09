# 197. Introdução ao gerenciador de geometria de grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de geometria")
root.geometry("600x400+650+300")

root.columnconfigure(index=0, weight=2)
root.rowconfigure(index=0, weight=1)

root.mainloop()