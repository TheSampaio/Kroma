import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()

# Create a StringVar to hold the current value of the combobox
current_var = tk.StringVar()

# Create the combobox
combobox = ttk.Combobox(window, textvariable=current_var)

# Set the list of values for the combobox
combobox['values'] = ('value1', 'value2', 'value3')

# Set the default value
combobox.set('value1')  # This will set 'value1' as the default value

# Alternatively, you can use the StringVar to set the default value
current_var.set('value1')  # This will also set 'value1' as the default value

combobox.pack()

window.mainloop()
