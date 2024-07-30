# Exploring Tk Themed Widgets 🎨

Introduction to themed Tk widgets and their customization. Tkinter provides a set of themed widgets that allow for a more modern and visually appealing GUI. These widgets are part of the `ttk` module, which stands for "themed Tk."

## Getting Started

First, make sure to import the `ttk` module from `tkinter`.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.title("Themed Widgets Example")
```

### 3. 🎨 **Using Themed Widgets**

The `ttk` module provides several widgets that are similar to the standard Tkinter widgets but come with a modern look and feel.

#### Example: Button

```python
# Create a themed Button widget
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)
```

#### Example: Label

```python
# Create a themed Label widget
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)
```

#### Example: Entry

```python
# Create a themed Entry widget
entry = ttk.Entry(root)
entry.pack(pady=10)
```

### 4. 🔧 **Customizing Themed Widgets**

You can customize the appearance of themed widgets using styles. The `ttk.Style` class is used to configure and query the styles.

#### Example: Customizing a Button

```python
style = ttk.Style()

# Configure the style
style.configure("TButton",
                font=("Helvetica", 12),
                foreground="blue")

# Apply the style to a Button
button = ttk.Button(root, text="Styled Button", style="TButton")
button.pack(pady=10)
```

#### Example: Customizing a Label

```python
style.configure("TLabel",
                font=("Helvetica", 12),
                foreground="green")

# Apply the style to a Label
label = ttk.Label(root, text="Styled Label", style="TLabel")
label.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage and customization of themed widgets:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Themed Widgets Example")

# Create and pack themed widgets
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)

label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=10)

# Customize the styles
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 12),
                foreground="blue")

style.configure("TLabel",
                font=("Helvetica", 12),
                foreground="green")

# Apply styles to widgets
styled_button = ttk.Button(root, text="Styled Button", style="TButton")
styled_button.pack(pady=10)

styled_label = ttk.Label(root, text="Styled Label", style="TLabel")
styled_label.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `themed_widgets.py` and run it using the Python interpreter:

```sh
python themed_widgets.py
```

You should see a window with several themed widgets and their customized styles.

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
                   