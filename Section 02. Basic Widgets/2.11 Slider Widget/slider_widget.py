import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Slider Widget Example")

# Create and pack a Slider widget
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=300)
slider.pack(pady=20)

# Function to show the slider value
def show_slider_value():
    print("Slider Value:", slider.get())

# Create and pack a Button to show the slider value
button = ttk.Button(root, text="Show Slider Value", command=show_slider_value)
button.pack(pady=10)

# Run the application
root.mainloop()