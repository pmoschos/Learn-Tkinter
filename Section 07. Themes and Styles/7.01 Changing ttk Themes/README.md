# Changing ttk Themes 🎨

Learn how to change the default ttk theme to a new one in Tkinter. Using different themes can enhance the look and feel of your application.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🎨 **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Changing ttk Themes Demo')
```

### 3. 🎨 **Changing the ttk Theme**

You can change the ttk theme using the `ttk.Style` class.

```python
# Create a style object
style = ttk.Style()

# Print available themes
print("Available themes:", style.theme_names())

# Set the theme
style.theme_use('clam')  # Change 'clam' to any available theme
```

### 4. 🎨 **Creating Widgets**

Create some widgets to see the effect of the theme change.

```python
# Create a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to change the ttk theme:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Changing ttk Themes Demo')

# Create a style object
style = ttk.Style()

# Print available themes
print("Available themes:", style.theme_names())

# Set the theme
style.theme_use('clam')  # Change 'clam' to any available theme

# Create a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `changing_ttk_themes.py` and run it using the Python interpreter:

```sh
python changing_ttk_themes.py
```

You should see a window with a label and a button using the new theme.

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
