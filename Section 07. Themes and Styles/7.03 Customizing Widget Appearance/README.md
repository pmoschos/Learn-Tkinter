# Customizing Widget Appearance ✨

Understand ttk elements and how to use them to change the appearance of widgets in Tkinter. Customizing widget appearance allows for a more personalized and visually appealing application.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. ✨ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Customizing Widget Appearance Demo')
```

### 3. ✨ **Understanding ttk Elements**

ttk elements are the building blocks of ttk widgets. You can customize these elements to change the appearance of widgets.

```python
# Create a style object
style = ttk.Style()

# Print available elements for a button
print("Button elements:", style.element_names('TButton'))
```

### 4. ✨ **Customizing Widget Appearance**

You can customize widget appearance by modifying elements and options.

```python
# Create a custom style for the button
style.configure('Custom.TButton',
                font=('Helvetica', 12),
                foreground='white',
                background='blue',
                padding=10,
                relief='flat')

# Modify the background color on hover
style.map('Custom.TButton',
          background=[('active', 'lightblue')],
          relief=[('pressed', 'sunken')])
```

### 5. ✨ **Creating Widgets with Custom Appearance**

Create some widgets using the custom appearance.

```python
# Create a label with the default style
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button with the custom style
button = ttk.Button(root, text="Click Me", style='Custom.TButton')
button.pack(pady=10)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating how to customize widget appearance:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Customizing Widget Appearance Demo')

# Create a style object
style = ttk.Style()

# Print available elements for a button
print("Button elements:", style.element_names('TButton'))

# Create a custom style for the button
style.configure('Custom.TButton',
                font=('Helvetica', 12),
                foreground='white',
                background='blue',
                padding=10,
                relief='flat')

# Modify the background color on hover
style.map('Custom.TButton',
          background=[('active', 'lightblue')],
          relief=[('pressed', 'sunken')])

# Create a label with the default style
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button with the custom style
button = ttk.Button(root, text="Click Me", style='Custom.TButton')
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `customizing_widget_appearance.py` and run it using the Python interpreter:

```sh
python customizing_widget_appearance.py
```

You should see a window with a label and a button with customized appearance.

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
