import tkinter as tk
from tkinter import messagebox

# Create an instance of Tkinter frame
root = tk.Tk()

# Set the geometry of the Tkinter frame
root.geometry("300x150")

# Function to open a message box
def open_msg_box():
    messagebox.showinfo("Title", "This is a message box")

# Create a button that will open the message box
button = tk.Button(root, text="Open Message Box", command=open_msg_box)
button.pack(pady=20)

# Run the event loop
root.mainloop()
