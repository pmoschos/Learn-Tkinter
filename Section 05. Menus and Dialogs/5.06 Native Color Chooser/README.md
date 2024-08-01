# Native Color Chooser 🎨

Learn how to display the native color-chooser dialog in Tkinter. The color chooser dialog allows users to select colors using the operating system's native color picker.

## Getting Started

First, make sure to import Tkinter and the `colorchooser` module.

### 1. 📦 **Importing Tkinter and the colorchooser module**

```python
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Native Color Chooser Demo')
```

### 3. 🎨 **Displaying the Color Chooser Dialog**

You can display the color chooser dialog using the `colorchooser.askcolor` method.

```python
# Function to display the color chooser dialog
def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    print(f"Selected color: {color_code}")

# Create a button to trigger the color chooser dialog
color_button = ttk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=20)
```

### 4. 📑 **Complete Code**

Here's the complete code demonstrating how to display the native color chooser dialog:

```python
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Native Color Chooser Demo')

# Function to display the color chooser dialog
def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    print(f"Selected color: {color_code}")

# Create a button to trigger the color chooser dialog
color_button = ttk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=20)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `native_color_chooser.py` and run it using the Python interpreter:

```sh
python native_color_chooser.py
```

You should see a window with a button that displays the native color chooser dialog when clicked.

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
