# 160. Centralizar a janela na tela

import tkinter as tk

root = tk.Tk()

root.title("Noite feliz")

# Definir o tamanho da janela por variaveis
window_width = 600
window_height = 500

# Obter as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Encontrar o ponto central
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# Definir a posição da janela no centro da tela

# As chaves {} faz ser possivel puxar o valor de uma variavel dentro de uma string
# o f indica que é um string formatada
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.mainloop()