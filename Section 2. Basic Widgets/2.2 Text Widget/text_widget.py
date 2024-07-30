import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Text Widget Example")

# Create and pack a Text widget
text = tk.Text(root, width=40, height=10)
text.pack(padx=10, pady=10)

# Configure the Text widget
text.config(wrap='word', font=("Helvetica", 12))

# Add a vertical scrollbar to the Text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y')
text.config(yscrollcommand=scrollbar.set)

# Run the application
root.mainloop()