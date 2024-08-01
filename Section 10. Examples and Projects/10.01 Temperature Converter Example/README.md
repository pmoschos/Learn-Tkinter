# Temperature Converter Example 🌡️

Build a simple application that converts a temperature from Fahrenheit to Celsius using Tkinter.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🌡️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('300x250')
root.title('Temperature Converter')
```

### 3. 🌡️ **Defining the Conversion Function**

Create a function that converts Fahrenheit to Celsius.

```python
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0
```

### 4. 🌡️ **Creating the UI Elements**

Create labels, entry widgets, and a button.

```python
# Fahrenheit label and entry
fahrenheit_label = ttk.Label(root, text="Fahrenheit:")
fahrenheit_label.pack(pady=5)

fahrenheit_var = tk.StringVar()
fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_var)
fahrenheit_entry.pack(pady=5)

# Celsius label
celsius_label = ttk.Label(root, text="Celsius:")
celsius_label.pack(pady=5)

celsius_var = tk.StringVar()
celsius_entry = ttk.Entry(root, textvariable=celsius_var, state='readonly')
celsius_entry.pack(pady=5)
```

### 5. 🌡️ **Creating the Conversion Button**

Create a button to trigger the conversion.

```python
def convert_temperature():
    try:
        fahrenheit = float(fahrenheit_var.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        celsius_var.set(f"{celsius:.2f}")
    except ValueError:
        celsius_var.set("Invalid input")

convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating how to build a temperature converter application:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('300x250')
root.title('Temperature Converter')

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

# Fahrenheit label and entry
fahrenheit_label = ttk.Label(root, text="Fahrenheit:")
fahrenheit_label.pack(pady=5)

fahrenheit_var = tk.StringVar()
fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_var)
fahrenheit_entry.pack(pady=5)

# Celsius label
celsius_label = ttk.Label(root, text="Celsius:")
celsius_label.pack(pady=5)

celsius_var = tk.StringVar()
celsius_entry = ttk.Entry(root, textvariable=celsius_var, state='readonly')
celsius_entry.pack(pady=5)

# Function to convert temperature and update the Celsius entry
def convert_temperature():
    try:
        fahrenheit = float(fahrenheit_var.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        celsius_var.set(f"{celsius:.2f}")
    except ValueError:
        celsius_var.set("Invalid input")

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `temperature_converter.py` and run it using the Python interpreter:

```sh
python temperature_converter.py
```

You should see a window with entry fields for Fahrenheit and Celsius temperatures and a button to convert the temperature.

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
