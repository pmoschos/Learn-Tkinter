# Spinbox Widget 🔢

Learn how to use a Spinbox widget in Tkinter. The Spinbox widget allows users to select a value from a range of values using arrow buttons.

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
root.title("Spinbox Widget Example")
```

### 3. 🔢 **Creating a Spinbox Widget**

You can create a Spinbox widget using the `Spinbox` class.

```python
# Create a Spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=100)
spinbox.pack(pady=20)
```

### 4. 🔄 **Retrieving the Spinbox Value**

You can retrieve the value of the spinbox using the `get` method.

```python
def show_spinbox_value():
    print("Spinbox Value:", spinbox.get())

# Create a Button to show the spinbox value
button = ttk.Button(root, text="Show Spinbox Value", command=show_spinbox_value)
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Spinbox widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Spinbox Widget Example")

# Create and pack a Spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=100)
spinbox.pack(pady=20)

# Function to show the spinbox value
def show_spinbox_value():
    print("Spinbox Value:", spinbox.get())

# Create and pack a Button to show the spinbox value
button = ttk.Button(root, text="Show Spinbox Value", command=show_spinbox_value)
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `spinbox_widget.py` and run it using the Python interpreter:

```sh
python spinbox_widget.py
```

You should see a window with a Spinbox widget allowing you to select a value, and a button to show the selected value.

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
