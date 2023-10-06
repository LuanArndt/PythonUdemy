# 174. Vinculando eventos à janela raiz

import tkinter as tk
from tkinter import ttk

def log(event):
    print(event)

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")

root.bind("<Any-KeyPress>", log)

root.mainloop()