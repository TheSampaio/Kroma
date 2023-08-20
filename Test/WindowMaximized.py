import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")

    button = tk.Button(root, text="Button")
    button.pack()

    root.mainloop()
