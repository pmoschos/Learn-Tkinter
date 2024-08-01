# Dynamic Styling Based on State ⚡

Learn how to dynamically change the appearance of a widget based on its specific state in Tkinter. This guide covers how to use the `map` method to customize widget styles for different states.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. ⚡ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Dynamic Styling Based on State Demo')
```

### 3. ⚡ **Creating a Custom Style with Dynamic States**

You can create a custom style and use the `map` method to define styles for different states.

```python
# Create a style object
style = ttk.Style()

# Create a custom style for the button
style.configure('Dynamic.TButton',
                font=('Helvetica', 12),
                foreground='black',
                background='lightgray',
                padding=10)

# Modify the style based on the button state
style.map('Dynamic.TButton',
          foreground=[('pressed', 'white'), ('active', 'blue')],
          background=[('pressed', 'blue'), ('active', 'lightblue')],
          relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
```

### 4. ⚡ **Creating Widgets with Dynamic Styling**

Create a button using the custom dynamic style.

```python
# Create a button with the dynamic style
button = ttk.Button(root, text="Dynamic Button", style='Dynamic.TButton')
button.pack(pady=20)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to dynamically change the appearance of a widget based on its specific state:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Dynamic Styling Based on State Demo')

# Create a style object
style = ttk.Style()

# Create a custom style for the button
style.configure('Dynamic.TButton',
                font=('Helvetica', 12),
                foreground='black',
                background='lightgray',
                padding=10)

# Modify the style based on the button state
style.map('Dynamic.TButton',
          foreground=[('pressed', 'white'), ('active', 'blue')],
          background=[('pressed', 'blue'), ('active', 'lightblue')],
          relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

# Create a button with the dynamic style
button = ttk.Button(root, text="Dynamic Button", style='Dynamic.TButton')
button.pack(pady=20)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `dynamic_styling.py` and run it using the Python interpreter:

```sh
python dynamic_styling.py
```

You should see a window with a button that changes its appearance based on its state.

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
