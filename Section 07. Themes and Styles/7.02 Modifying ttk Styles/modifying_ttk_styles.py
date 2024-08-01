import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Modifying ttk Styles Demo')

# Create a style object
style = ttk.Style()

# Create a custom style for the button
style.configure('Custom.TButton',
                font=('Helvetica', 12),
                foreground='white',
                background='blue',
                padding=10)

# Create a custom style for the label
style.configure('Custom.TLabel',
                font=('Helvetica', 14),
                foreground='blue',
                background='white',
                padding=10)

# Create a label with the custom style
label = ttk.Label(root, text="Hello, Tkinter!", style='Custom.TLabel')
label.pack(pady=20)

# Create a button with the custom style
button = ttk.Button(root, text="Click Me", style='Custom.TButton')
button.pack(pady=10)

# Run the application
root.mainloop()