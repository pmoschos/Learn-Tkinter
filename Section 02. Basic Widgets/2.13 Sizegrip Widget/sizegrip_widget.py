import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Sizegrip Widget Example")
root.geometry("300x200")

# Create and pack a Sizegrip widget
sizegrip = ttk.Sizegrip(root)
sizegrip.pack(side="right", anchor="se")

# Run the application
root.mainloop()