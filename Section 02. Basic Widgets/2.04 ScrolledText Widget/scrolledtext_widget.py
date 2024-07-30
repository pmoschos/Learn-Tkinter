import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Create the main window
root = tk.Tk()
root.title("ScrolledText Widget Example")

# Create and pack a ScrolledText widget
scrolled_text = ScrolledText(root, width=40, height=10, wrap='word')
scrolled_text.pack(padx=10, pady=10)

# Add content to the ScrolledText widget
sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""

scrolled_text.insert('1.0', sample_text)

# Run the application
root.mainloop()