import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Customizing Widget Appearance Demo')

# Create a style object
style = ttk.Style()

# Print available elements for a button
print("Button elements:", style.element_names('TButton'))

# Create a custom style for the button
style.configure('Custom.TButton',
                font=('Helvetica', 12),
                foreground='white',
                background='blue',
                padding=10,
                relief='flat')

# Modify the background color on hover
style.map('Custom.TButton',
          background=[('active', 'lightblue')],
          relief=[('pressed', 'sunken')])

# Create a label with the default style
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button with the custom style
button = ttk.Button(root, text="Click Me", style='Custom.TButton')
button.pack(pady=10)

# Run the application
root.mainloop()