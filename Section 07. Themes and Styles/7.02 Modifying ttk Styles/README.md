# Modifying ttk Styles 🖌️

Learn how to change the appearance of widgets by modifying or extending the ttk style in Tkinter. Customizing styles can enhance the look and feel of your application.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🖌️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Modifying ttk Styles Demo')
```

### 3. 🖌️ **Creating a Custom Style**

You can create a custom style using the `ttk.Style` class and modify the appearance of widgets.

```python
# Create a style object
style = ttk.Style()

# Create a custom style for the button
style.configure('Custom.TButton',
                font=('Helvetica', 12),
                foreground='white',
                background='blue',
                padding=10)

# Create a custom style for the label
style.configure('Custom.TLabel',
                font=('Helvetica', 14),
                foreground='blue',
                background='white',
                padding=10)
```

### 4. 🖌️ **Creating Widgets with Custom Styles**

Create some widgets using the custom styles.

```python
# Create a label with the custom style
label = ttk.Label(root, text="Hello, Tkinter!", style='Custom.TLabel')
label.pack(pady=20)

# Create a button with the custom style
button = ttk.Button(root, text="Click Me", style='Custom.TButton')
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to modify ttk styles:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Modifying ttk Styles Demo')

# Create a style object
style = ttk.Style()

# Create a custom style for the button
style.configure('Custom.TButton',
                font=('Helvetica', 12),
                foreground='white',
                background='blue',
                padding=10)

# Create a custom style for the label
style.configure('Custom.TLabel',
                font=('Helvetica', 14),
                foreground='blue',
                background='white',
                padding=10)

# Create a label with the custom style
label = ttk.Label(root, text="Hello, Tkinter!", style='Custom.TLabel')
label.pack(pady=20)

# Create a button with the custom style
button = ttk.Button(root, text="Click Me", style='Custom.TButton')
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `modifying_ttk_styles.py` and run it using the Python interpreter:

```sh
python modifying_ttk_styles.py
```

You should see a window with a label and a button using the custom styles.

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
