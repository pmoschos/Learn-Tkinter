# Checkbox Widget ☑️

Learn how to create and use a checkbox widget in Tkinter. The Checkbox widget allows users to make a binary choice, such as Yes/No or On/Off.

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
root.title("Checkbox Widget Example")
```

### 3. ☑️ **Creating a Checkbox Widget**

You can create a Checkbox widget using the `Checkbutton` class.

```python
# Variable to store the state of the checkbox
checkbox_var = tk.BooleanVar()

# Create a Checkbox widget
checkbox = ttk.Checkbutton(root, text="Accept Terms and Conditions", variable=checkbox_var)
checkbox.pack(pady=10)
```

### 4. 🔄 **Retrieving the Checkbox State**

You can retrieve the state of the checkbox using the `get` method of the variable.

```python
def show_state():
    print("Checkbox State:", checkbox_var.get())

# Create a Button to show the state of the checkbox
button = ttk.Button(root, text="Show State", command=show_state)
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Checkbox widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Checkbox Widget Example")

# Variable to store the state of the checkbox
checkbox_var = tk.BooleanVar()

# Create and pack a Checkbox widget
checkbox = ttk.Checkbutton(root, text="Accept Terms and Conditions", variable=checkbox_var)
checkbox.pack(pady=10)

# Function to show the state of the checkbox
def show_state():
    print("Checkbox State:", checkbox_var.get())

# Create and pack a Button to show the state of the checkbox
button = ttk.Button(root, text="Show State", command=show_state)
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `checkbox_widget.py` and run it using the Python interpreter:

```sh
python checkbox_widget.py
```

You should see a window with a Checkbox widget and a button to show its state.

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
