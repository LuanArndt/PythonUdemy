# 163. Transparência da janela

import tkinter as tk
root = tk.Tk()
root.title("Noite feliz")
root.geometry("200x200+100-100")

# Alterar canal alpha (de 0.0 até 1.0)
root.attributes("-alpha", 0.8)

root.mainloop()