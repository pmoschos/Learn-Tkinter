# Slider Widget 🔄

Learn how to create and use a slider with the Tkinter Scale widget. The Scale widget allows users to select a numerical value by moving a slider along a scale.

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
root.title("Slider Widget Example")
```

### 3. 🔄 **Creating a Slider Widget**

You can create a Slider widget using the `Scale` class.

```python
# Create a Slider widget
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=300)
slider.pack(pady=20)
```

### 4. 🔄 **Retrieving the Slider Value**

You can retrieve the value of the slider using the `get` method.

```python
def show_slider_value():
    print("Slider Value:", slider.get())

# Create a Button to show the slider value
button = ttk.Button(root, text="Show Slider Value", command=show_slider_value)
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Slider widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Slider Widget Example")

# Create and pack a Slider widget
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=300)
slider.pack(pady=20)

# Function to show the slider value
def show_slider_value():
    print("Slider Value:", slider.get())

# Create and pack a Button to show the slider value
button = ttk.Button(root, text="Show Slider Value", command=show_slider_value)
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `slider_widget.py` and run it using the Python interpreter:

```sh
python slider_widget.py
```

You should see a window with a Slider widget allowing you to select a value, and a button to show the selected value.

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
