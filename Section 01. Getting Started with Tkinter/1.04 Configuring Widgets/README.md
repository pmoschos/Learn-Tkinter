# Configuring Widgets ⚙️

Learn various methods to set options for a widget in Tkinter. Configuring widgets allows you to customize their appearance and behavior to suit your application's needs.

## Getting Started

First, make sure to import Tkinter.

### 1. 📦 **Importing Tkinter**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.title("Configuring Widgets Example")
```

### 3. ⚙️ **Configuring Widget Options**

You can set options for a widget when you create it or later using the `config` method.

#### Example: Button

Create a Button widget with initial options:

```python
button = tk.Button(root, text="Click Me", fg="white", bg="blue")
button.pack(pady=10)
```

Configure the Button widget's options later:

```python
button.config(text="Press Me", fg="black", bg="red")
```

#### Example: Label

Create a Label widget with initial options:

```python
label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=10)
```

Configure the Label widget's options later:

```python
label.config(text="Hello, World!", font=("Arial", 20), fg="green")
```

### 4. 🔄 **Dynamic Configuration**

You can also change widget options dynamically based on events.

#### Example: Button with Dynamic Configuration

```python
def change_button_text():
    button.config(text="You Clicked Me!")

button = tk.Button(root, text="Click Me", command=change_button_text)
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating various methods to configure widgets:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Configuring Widgets Example")

# Create and pack a Button widget with initial options
button = tk.Button(root, text="Click Me", fg="white", bg="blue")
button.pack(pady=10)

# Configure the Button widget's options later
button.config(text="Press Me", fg="black", bg="red")

# Create and pack a Label widget with initial options
label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=10)

# Configure the Label widget's options later
label.config(text="Hello, World!", font=("Arial", 20), fg="green")

# Function to change button text dynamically
def change_button_text():
    button.config(text="You Clicked Me!")

# Create and pack a Button widget with dynamic configuration
dynamic_button = tk.Button(root, text="Click Me", command=change_button_text)
dynamic_button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `configuring_widgets.py` and run it using the Python interpreter:

```sh
python configuring_widgets.py
```

You should see a window demonstrating various ways to configure widget options.

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
