# 221. Tkinter Progressbar no exemplo de modo indeterminate

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400+750+750")
root.grid()

pb = ttk.Progressbar(
    root,
    orient=tk.HORIZONTAL,
    length=300,
    mode="indeterminate"
)

pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

start_button = ttk.Button(
    root,
    text="Start",
    command=lambda: pb.start(10)
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text="Stop",
    command=lambda: pb.stop()
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()