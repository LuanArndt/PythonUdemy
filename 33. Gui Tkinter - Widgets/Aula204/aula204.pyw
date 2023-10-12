# 210. Tkinter Combobox

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

selected_day = tk.StringVar()

def day_changed(event):
    showinfo("Resultado", f"Você selecionou {selected_day.get()}")

day_cb = ttk.Combobox(
    root, 
    state='readonly',
    textvariable=selected_day
)
day_cb["values"] = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
selected_day.set("Segunda")
day_cb.pack(fill=tk.X, padx=5,pady=5)
day_cb.bind("<<ComboboxSelected>>", day_changed)

root.mainloop()