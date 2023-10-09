# 202. Introdução ao widget Tkinter Text

from tkinter import Tk, Text

root = Tk()
root.title("Python Tkinter")

text = Text(
    root,
    height=8,
    width=10,
    font="Arial 24",
    background="yellow",
    foreground="red"
)

text.pack()

root.mainloop()