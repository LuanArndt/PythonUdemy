# 159. Alterar o tamanho e localização da janela

import tkinter as tk

root = tk.Tk()

root.title("Noite feliz")

# 600x400 = Tamanho da janela X e Y
# -100 + 300 = Afastamento das bordas da tela. O valor negativo quer dizer que o afastamento sera em relação a borda esquerda ou da borda inferior. 
root.geometry("600x400+100-100")

# Agora ele não vai redimencionar conforme o meu widget. Ex:
lbl = tk.Label(root, text="Update")
lbl.pack()

root.mainloop()