# 164. Ordem de emplilhamento da janela

import tkinter as tk
root = tk.Tk()
root.title("Noite feliz")
root.geometry("200x200+100-100")

# Garantir que a janela vai ficar sempre no topo (Não vai ser sobreposta por nenhuma outra janela)
#root.attributes("-topmost", 1)

# Para mover uma janela para cima
#root.lift()

# Para mover uma janela para baixo
root.lower()


root.mainloop()