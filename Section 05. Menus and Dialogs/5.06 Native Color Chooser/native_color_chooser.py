import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Native Color Chooser Demo')

# Function to display the color chooser dialog
def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    print(f"Selected color: {color_code}")

# Create a button to trigger the color chooser dialog
color_button = ttk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=20)

# Run the application
root.mainloop()