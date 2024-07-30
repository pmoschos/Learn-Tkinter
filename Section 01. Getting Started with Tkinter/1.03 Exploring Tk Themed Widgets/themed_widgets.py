import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Themed Widgets Example")

# Create and pack themed widgets
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)

label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=10)

# Customize the styles
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),
                foreground="blue")

style.configure("TLabel",
                font=("Helvetica", 14),
                foreground="green")

# Apply styles to widgets
styled_button = ttk.Button(root, text="Styled Button", style="TButton")
styled_button.pack(pady=10)

styled_label = ttk.Label(root, text="Styled Label", style="TLabel")
styled_label.pack(pady=10)

# Run the application
root.mainloop()