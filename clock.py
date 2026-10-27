import tkinter as tk
from time import strftime

root = tk.Tk()
clock = tk.Label(root, font=("Arial", 40))
clock.pack(padx=20, pady=20)

def update():
    clock.config(text=strftime("%H:%M:%S"))
    root.after(1000, update)

update()
root.mainloop()