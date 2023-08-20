import tkinter as tk

# Create the root window
root = tk.Tk()

# Create buttons with different text
button1 = tk.Button(root, text="Top left")
button2 = tk.Button(root, text="Top right")
button3 = tk.Button(root, text="Bottom left")
button4 = tk.Button(root, text="Bottom right")
button5 = tk.Button(root, text="Top")
button6 = tk.Button(root, text="Bottom")
button7 = tk.Button(root, text="Left")
button8 = tk.Button(root, text="Right")
button9 = tk.Button(root, text="Center")

# Use the place method to position the buttons in the corners of the window
button1.place(x=0, y=0, anchor="nw")
button2.place(relx=1.0, y=0, anchor="ne")
button3.place(x=0, rely=1.0, anchor="sw")
button4.place(relx=1.0, rely=1.0, anchor="se")
button5.place(relx=0.5, y=0, anchor="n")
button6.place(relx=0.5, rely=1.0, anchor="s")
button7.place(x=0, rely=0.5, anchor="w")
button8.place(relx=1.0, rely=0.5, anchor="e")
button9.place(relx=0.5, rely=0.5)

# Run the main loop
root.mainloop()
