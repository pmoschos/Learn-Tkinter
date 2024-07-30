import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Separator Widget Example")

# Add a Label widget above the Separator
label1 = ttk.Label(root, text="Above the separator")
label1.pack(pady=5)

# Create and pack a Separator widget
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

# Add a Label widget below the Separator
label2 = ttk.Label(root, text="Below the separator")
label2.pack(pady=5)

# Run the application
root.mainloop()