import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Custom Widgets Demo')

class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.change_color)

    def change_color(self, event):
        colors = ["red", "green", "blue", "yellow", "pink"]
        current_color = self.cget("bg")
        next_color = colors[(colors.index(current_color) + 1) % len(colors)]
        self.config(bg=next_color)

# Create an instance of CustomLabel
custom_label = CustomLabel(root, text="Click me to change my color", bg="red", fg="white", font=("Arial", 16))
custom_label.pack(pady=50)

# Run the application
root.mainloop()