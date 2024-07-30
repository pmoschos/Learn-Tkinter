# Combobox Widget 📑

Learn how to create and use a combobox widget in Tkinter. The Combobox widget allows users to select an option from a dropdown list.

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
root.title("Combobox Widget Example")
```

### 3. 📑 **Creating a Combobox Widget**

You can create a Combobox widget using the `Combobox` class.

```python
# Variable to store the selected option
selected_option = tk.StringVar()

# Create a Combobox widget
combobox = ttk.Combobox(root, textvariable=selected_option)
combobox['values'] = ("Option 1", "Option 2", "Option 3")
combobox.pack(pady=10)
```

### 4. 🔄 **Retrieving the Selected Option**

You can retrieve the state of the selected option using the `get` method of the variable.

```python
def show_selected_option():
    print("Selected Option:", selected_option.get())

# Create a Button to show the selected option
button = ttk.Button(root, text="Show Selected Option", command=show_selected_option)
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Combobox widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Combobox Widget Example")

# Variable to store the selected option
selected_option = tk.StringVar()

# Create and pack a Combobox widget
combobox = ttk.Combobox(root, textvariable=selected_option)
combobox['values'] = ("Option 1", "Option 2", "Option 3")
combobox.pack(pady=10)

# Function to show the selected option
def show_selected_option():
    print("Selected Option:", selected_option.get())

# Create and pack a Button to show the selected option
button = ttk.Button(root, text="Show Selected Option", command=show_selected_option)
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `combobox_widget.py` and run it using the Python interpreter:

```sh
python combobox_widget.py
```

You should see a window with a Combobox widget allowing you to select one of several options, and a button to show the selected option.

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
