# 214. Tkinter Slider

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")

current_value = tk.DoubleVar()

def slider_changed(event):
    #print(current_value.get())
    print(slider.get())
    
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    variable=current_value,
    command=slider_changed
)

slider.pack()

root.mainloop()