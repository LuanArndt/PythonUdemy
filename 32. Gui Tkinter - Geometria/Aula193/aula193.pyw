# 199. Exemplo de uso do gerenciador de geometria grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login")
root.geometry("240x100+750+400")

# Configurar o grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Username
username_lable = ttk.Label(root, text="Username:")
username_lable.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# Password
password_lable = ttk.Label(root, text="Password:")
password_lable.grid(column=0,row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# Login button
btn1 = ttk.Button(root, text="Login")
btn1.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

root.mainloop()