# Command Binding and Events 🖇️

Master the use of command binding and handling events in Tkinter. This guide covers how to bind commands to widgets and handle various events effectively.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Command Binding and Events Demo')
```

### 3. 🖇️ **Binding Commands to Widgets**

You can bind commands to widgets using the `command` option.

```python
# Command function for button
def on_button_click():
    print("Button clicked!")

# Create a button and bind the command
button = ttk.Button(root, text='Click Me', command=on_button_click)
button.pack(pady=20)
```

### 4. 🖇️ **Binding Events to Widgets**

You can bind events to widgets using the `bind` method.

```python
# Event handler function for key press
def on_key_press(event):
    print(f"Key pressed: {event.char}")

# Create an entry widget and bind the key press event
entry = ttk.Entry(root)
entry.pack(pady=20)
entry.bind('<KeyPress>', on_key_press)
```

### 5. 🖇️ **Handling Mouse Events**

You can handle mouse events such as clicks and motion.

```python
# Event handler function for mouse click
def on_mouse_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")

# Create a label and bind the mouse click event
label = ttk.Label(root, text='Click anywhere on this label')
label.pack(pady=20)
label.bind('<Button-1>', on_mouse_click)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating command binding and handling events:

```python
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
```

## Running the Code

Save your code in a file named `command_binding_events.py` and run it using the Python interpreter:

```sh
python command_binding_events.py
```

You should see a window demonstrating command binding and handling various events.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧

Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
