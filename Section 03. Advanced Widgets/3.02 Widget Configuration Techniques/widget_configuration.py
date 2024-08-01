import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Widget Configuration Techniques Demo')

# Method 1: Using Keyword Arguments
label1 = ttk.Label(root, text="This is a label", font=("Arial", 14), foreground="blue", background="yellow")
label1.pack(pady=10)

# Method 2: Using the config Method
label2 = ttk.Label(root)
label2.pack(pady=10)
label2.config(text="This is another label", font=("Arial", 14), foreground="green", background="lightgray")

# Method 3: Using the Option Database
root.option_add('*TButton.Foreground', 'red')
button = ttk.Button(root, text="This is a button")
button.pack(pady=10)

# Changing Widget States
entry = ttk.Entry(root)
entry.pack(pady=10)
entry.state(['disabled'])  # Disable the entry widget
entry.state(['!disabled'])  # Enable the entry widget

# Run the application
root.mainloop()