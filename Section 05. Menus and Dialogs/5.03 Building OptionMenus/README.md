# Building OptionMenus 📂

Learn how to create an OptionMenu widget that provides a list of options in a drop-down menu in Tkinter. The OptionMenu widget is useful for allowing users to select from a predefined list of options.

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
root.title('Building OptionMenus Demo')
```

### 3. 📂 **Creating an OptionMenu**

You can create an OptionMenu widget using the `OptionMenu` class.

```python
# Define the variable to store the selected option
selected_option = tk.StringVar()
selected_option.set("Option 1")  # Set default value

# Create an OptionMenu widget
option_menu = ttk.OptionMenu(root, selected_option, "Option 1", "Option 1", "Option 2", "Option 3")
option_menu.pack(pady=20)
```

### 4. 📂 **Handling Option Selection**

You can define a function to handle the selection of an option.

```python
# Function to handle the selection of an option
def handle_selection(event):
    print(f"Selected option: {selected_option.get()}")

# Bind the function to the variable
selected_option.trace("w", handle_selection)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to build an OptionMenu widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Building OptionMenus Demo')

# Define the variable to store the selected option
selected_option = tk.StringVar()
selected_option.set("Option 1")  # Set default value

# Create an OptionMenu widget
option_menu = ttk.OptionMenu(root, selected_option, "Option 1", "Option 1", "Option 2", "Option 3")
option_menu.pack(pady=20)

# Function to handle the selection of an option
def handle_selection(*args):
    print(f"Selected option: {selected_option.get()}")

# Bind the function to the variable
selected_option.trace("w", handle_selection)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `building_optionmenus.py` and run it using the Python interpreter:

```sh
python building_optionmenus.py
```

You should see a window with an OptionMenu that provides a list of options in a drop-down menu.

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
