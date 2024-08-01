# Full Project Implementations 🔧

Explore full project implementations to consolidate your learning. This guide covers a comprehensive example of a Tkinter project.

## Project Overview

We will create a complete Tkinter application that includes the following features:
- Temperature Converter (Fahrenheit to Celsius)
- System Tray Integration
- Progress Bar with Threads

## Getting Started

First, make sure to install the necessary libraries.

### 1. 📦 **Installing Required Libraries**

Install `pystray` and `Pillow` for system tray integration.

```sh
pip install pystray pillow
```

### 2. 🔧 **Importing Required Libraries**

Import Tkinter, ttk, threading, pystray, and other necessary modules.

```python
import tkinter as tk
from tkinter import ttk
import threading
import time
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
```

### 3. 🔧 **Defining the Temperature Converter Function**

Create a function that converts Fahrenheit to Celsius.

```python
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0
```

### 4. 🔧 **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Full Project Implementation')
```

### 5. 🔧 **Creating the Temperature Converter UI**

Create labels, entry widgets, and a button for the temperature converter.

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
```

### 6. 🔧 **Creating the Progress Bar UI**

Create a progress bar widget and a function to update it in a separate thread.

```python
# Create a progress bar
progress = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
progress.pack(pady=20)

# Define a long-running task
def long_running_task():
    for i in range(100):
        time.sleep(0.1)  # Simulate a time-consuming task
        progress['value'] = i + 1
    progress['value'] = 100

# Start the task in a separate thread
def start_task():
    thread = threading.Thread(target=long_running_task)
    thread.start()

# Create a button to start the task
start_button = ttk.Button(root, text='Start Task', command=start_task)
start_button.pack(pady=10)
```

### 7. 🔧 **Creating the System Tray Icon**

Create an icon and menu for the system tray.

```python
def create_image():
    # Generate an image
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=(255, 0, 0))
    dc.rectangle(
        (0, 0, width // 2, height // 2),
        fill=(0, 255, 0))
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=(0, 0, 255))
    dc.rectangle(
        (width // 2, height // 2, width, height),
        fill=(255, 255, 0))
    return image

def on_quit(icon, item):
    icon.stop()
    root.quit()

icon = pystray.Icon("test_icon")
menu = (item('Quit', on_quit),)
icon.menu = pystray.Menu(*menu)
icon.icon = create_image()

def run_icon():
    icon.run()

icon_thread = threading.Thread(target=run_icon)
icon_thread.start()
```

### 8. 📑 **Complete Code**

Here's the complete code demonstrating a full project implementation in Tkinter:

```python
import tkinter as tk
from tkinter import ttk
import threading
import time
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Full Project Implementation')

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

# Create a progress bar
progress = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
progress.pack(pady=20)

# Define a long-running task
def long_running_task():
    for i in range(100):
        time.sleep(0.1)  # Simulate a time-consuming task
        progress['value'] = i + 1
    progress['value'] = 100

# Start the task in a separate thread
def start_task():
    thread = threading.Thread(target=long_running_task)
    thread.start()

# Create a button to start the task
start_button = ttk.Button(root, text='Start Task', command=start_task)
start_button.pack(pady=10)

# Create an icon and menu for the system tray
def create_image():
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=(255, 0, 0))
    dc.rectangle((0, 0, width // 2, height // 2), fill=(0, 255, 0))
    dc.rectangle((0, height // 2, width // 2, height), fill=(0, 0, 255))
    dc.rectangle((width // 2, height // 2, width, height), fill=(255, 255, 0))
    return image

def on_quit(icon, item):
    icon.stop()
    root.quit()

icon = pystray.Icon("test_icon")
menu = (item('Quit', on_quit),)
icon.menu = pystray.Menu(*menu)
icon.icon = create_image()

def run_icon():
    icon.run()

icon_thread = threading.Thread(target=run_icon)
icon_thread.start()

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `full_project_implementation.py` and run it using the Python interpreter:

```sh
python full_project_implementation.py
```

You should see a window with a temperature converter, a progress bar, and a system tray icon.

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
