# 233. Outro exemplo de uma janela orientada a objetos no Tkinter

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurar a janela principal:
        self.title('Minha aplicação POO')
        self.geometry('300x50+750+400')

        # label
        self.label = ttk.Label(self, text='Ola, tkinter')
        self.label.pack()

        # button
        self.btn = ttk.Button(self, text='Click me!')
        self.btn["command"] = self.button_clicked
        self.btn.pack()

    def button_clicked(self):
        showinfo(title='Informação', message='Ola, Tkinter!!!')

if __name__ == "__main__":
    app = App()
    app.mainloop()



