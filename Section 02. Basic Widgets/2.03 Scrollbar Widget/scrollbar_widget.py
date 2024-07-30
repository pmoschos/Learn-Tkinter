import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Scrollbar Widget Example")

# Create a Text widget
text = tk.Text(root, width=40, height=10, wrap='word')
text.pack(side='left', fill='both', expand=True, padx=10, pady=10)

# Create a Scrollbar widget and link it to the Text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y')

text.config(yscrollcommand=scrollbar.set)

# Add content to the Text widget
sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""

text.insert('1.0', sample_text)

# Run the application
root.mainloop()