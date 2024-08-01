# Validating User Input 🔍

Learn how to use Tkinter validation to validate user inputs. This guide covers how to create input validation using the `register` method and validatecommand option.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🔍 **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Validating User Input Demo')
```

### 3. 🔍 **Defining Validation Functions**

Create validation functions to check user inputs.

```python
def validate_number(action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if action != '1':  # If the action is not insertion, allow it
        return True
    if text in '0123456789':
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return False
```

### 4. 🔍 **Registering Validation Functions**

Register the validation functions with Tkinter.

```python
# Register the validation function
vcmd = (root.register(validate_number), '%d', '%P', '%s', '%S', '%v', '%V', '%W')
```

### 5. 🔍 **Creating Entry Widgets with Validation**

Create entry widgets that use the validation function.

```python
# Create a label
label = ttk.Label(root, text="Enter a number:")
label.pack(pady=10)

# Create an entry widget with validation
entry = ttk.Entry(root, validate='key', validatecommand=vcmd)
entry.pack(pady=10)

# Create a button to get the entry value
def get_value():
    print("Entered value:", entry.get())

button = ttk.Button(root, text="Submit", command=get_value)
button.pack(pady=10)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating how to validate user input in Tkinter:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Validating User Input Demo')

# Define the validation function
def validate_number(action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if action != '1':  # If the action is not insertion, allow it
        return True
    if text in '0123456789':
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return False

# Register the validation function
vcmd = (root.register(validate_number), '%d', '%P', '%s', '%S', '%v', '%V', '%W')

# Create a label
label = ttk.Label(root, text="Enter a number:")
label.pack(pady=10)

# Create an entry widget with validation
entry = ttk.Entry(root, validate='key', validatecommand=vcmd)
entry.pack(pady=10)

# Create a button to get the entry value
def get_value():
    print("Entered value:", entry.get())

button = ttk.Button(root, text="Submit", command=get_value)
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `validating_user_input.py` and run it using the Python interpreter:

```sh
python validating_user_input.py
```

You should see a window with an entry widget that only allows numeric input and a button to print the entered value.

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
