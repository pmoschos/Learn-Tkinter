import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("PanedWindow Widget Example")

# Create and pack a PanedWindow widget
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Add panes to the PanedWindow
left_frame = ttk.Frame(paned_window, width=100, height=300, relief=tk.SUNKEN)
paned_window.add(left_frame)

right_frame = ttk.Frame(paned_window, width=400, height=300, relief=tk.SUNKEN)
paned_window.add(right_frame)

# Run the application
root.mainloop()
