# 203. Inserindo e obtendo conteúdo do widget Text

from tkinter import Tk, Text, ttk

root = Tk()
root.title("Python Tkinter")

text = Text(
    root,
    height=10,
    width=20,
    font="Arial 24",
)

text.pack()

text.insert("1.0", "Este é um widget Text demo")
txt = text.get("1.0", "end")

print(txt)

root.mainloop()