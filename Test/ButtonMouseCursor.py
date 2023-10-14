from tkinter import *

def changeOnHover(button, cursorOnHover, cursorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(cursor=cursorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(cursor=cursorOnLeave))

root = Tk()
myButton = Button(root, text="Hover over me")
myButton.pack()
changeOnHover(myButton, "hand2", "arrow")
root.mainloop()
