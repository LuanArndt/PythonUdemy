# 173. Padrões de eventos

import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Tecla entre pressionada")

def log(event):
    print(event)
    print(f"keysym....: {event.keysym}")
    print(f"keycode...: {event.keycode}")
    print(f"keysym_num: {event.keysym_num}")
    print(f"char......: {event.char}")

root = tk.Tk()

root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

btn1 = ttk.Button(root, text="Executar")
btn1.bind("<Any-KeyPress>", log)
btn1.focus()
btn1.pack(expand=True)

root.mainloop()

# <modificador-tipo-detalhe>
# <KeyPress-A>
# <Alt-Control-KeyPress-KP_Delete>