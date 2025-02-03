import tkinter as tk

def open_window():
    top = tk.Toplevel(root)
    top.grab_set()
    label = tk.Label(top, text="This is the second window")
    label.pack()

root = tk.Tk()
button = tk.Button(root, text="Open Window", command=open_window)
button.pack()
root.mainloop()
