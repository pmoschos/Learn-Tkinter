import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Dynamic Styling Based on State Demo')

# Create a style object
style = ttk.Style()

# Create a custom style for the button
style.configure('Dynamic.TButton',
                font=('Helvetica', 12),
                foreground='black',
                background='lightgray',
                padding=10)

# Modify the style based on the button state
style.map('Dynamic.TButton',
          foreground=[('pressed', 'white'), ('active', 'blue')],
          background=[('pressed', 'blue'), ('active', 'lightblue')],
          relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

# Create a button with the dynamic style
button = ttk.Button(root, text="Dynamic Button", style='Dynamic.TButton')
button.pack(pady=20)

# Run the application
root.mainloop()