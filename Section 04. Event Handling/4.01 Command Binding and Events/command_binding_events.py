import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Command Binding and Events Demo')

# Command function for button
def on_button_click():
    print("Button clicked!")

# Create a button and bind the command
button = ttk.Button(root, text='Click Me', command=on_button_click)
button.pack(pady=20)

# Event handler function for key press
def on_key_press(event):
    print(f"Key pressed: {event.char}")

# Create an entry widget and bind the key press event
entry = ttk.Entry(root)
entry.pack(pady=20)
entry.bind('<KeyPress>', on_key_press)

# Event handler function for mouse click
def on_mouse_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")

# Create a label and bind the mouse click event
label = ttk.Label(root, text='Click anywhere on this label')
label.pack(pady=20)
label.bind('<Button-1>', on_mouse_click)

# Run the application
root.mainloop()