import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Binding Events to Widgets Demo')

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

# Event handler function for mouse motion
def on_mouse_motion(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

# Bind mouse motion event to the label
label.bind('<Motion>', on_mouse_motion)

# Event handler function for focus in
def on_focus_in(event):
    print("Entry gained focus")

# Event handler function for focus out
def on_focus_out(event):
    print("Entry lost focus")

# Bind focus events to the entry widget
entry.bind('<FocusIn>', on_focus_in)
entry.bind('<FocusOut>', on_focus_out)

# Run the application
root.mainloop()