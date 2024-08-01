import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Using Menubutton Demo')

# Create a Menubutton
menubutton = ttk.Menubutton(root, text='Options')
menubutton.pack(pady=20)

# Create a Menu and attach it to the Menubutton
menu = tk.Menu(menubutton, tearoff=0)
menubutton['menu'] = menu

# Add menu items to the Menu
menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
menu.add_command(label="Option 3", command=lambda: print("Option 3 selected"))

# Run the application
root.mainloop()