# Command Binding in Tkinter 🔗

Learn how to respond to events using command bindings in Tkinter. Command bindings allow you to connect actions (like button clicks) to functions in your code.

## Getting Started

First, make sure to import Tkinter.

### 1. 📦 **Importing Tkinter**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.title("Command Binding Example")
```

### 3. 🔗 **Binding Commands to Widgets**

You can bind commands to widgets to make them interactive.

#### Example: Button Command

Create a Button widget and bind it to a function.

```python
def on_button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)
```

### 4. 🔄 **Binding Events to Widgets**

You can also bind specific events to widgets using the `bind` method.

#### Example: Binding an Event to a Button

```python
def on_button_press(event):
    print("Button pressed!")

button = tk.Button(root, text="Press Me")
button.bind("<Button-1>", on_button_press)
button.pack(pady=10)
```

### 5. 🔑 **Common Events**

Here are some common events you can bind to widgets:

- `<Button-1>`: Left mouse button click
- `<Button-3>`: Right mouse button click
- `<Enter>`: Mouse pointer enters the widget
- `<Leave>`: Mouse pointer leaves the widget
- `<KeyPress>`: A key is pressed

### 6. 📑 **Complete Code**

Here's the complete code demonstrating command binding in Tkinter:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Command Binding Example")

# Function to handle button click
def on_button_click():
    print("Button clicked!")

# Create and pack a Button widget with command binding
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Function to handle button press event
def on_button_press(event):
    print("Button pressed!")

# Create and pack a Button widget with event binding
event_button = tk.Button(root, text="Press Me")
event_button.bind("<Button-1>", on_button_press)
event_button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `command_binding.py` and run it using the Python interpreter:

```sh
python command_binding.py
```

You should see a window with buttons that print messages to the console when clicked or pressed.

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
