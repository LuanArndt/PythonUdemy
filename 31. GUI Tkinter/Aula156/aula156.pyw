# 162. Estado inicial da janela

import tkinter as tk
root = tk.Tk()
root.title("Noite feliz")
root.geometry("200x200+100-100")

# Apresentar maximizada
#root.state("zoomed")

# Apresentar minimizada
#root.state("iconic")

# Apresentar normal (Já é o padrão)
root.state("normal")

root.mainloop()