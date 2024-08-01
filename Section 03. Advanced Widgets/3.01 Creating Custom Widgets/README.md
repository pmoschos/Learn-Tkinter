# Creating Custom Widgets 🔧

Learn how to create your own custom widgets in Tkinter. Custom widgets allow you to encapsulate functionality and reuse it across your application.

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
root.geometry('400x300')
root.title('Custom Widgets Demo')
```

### 3. 🔧 **Creating a Custom Widget**

You can create a custom widget by subclassing a Tkinter widget or combining multiple widgets.

### Example: CustomLabel

Here is an example of creating a custom label widget that changes color when clicked.

```python
class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.change_color)

    def change_color(self, event):
        colors = ["red", "green", "blue", "yellow", "pink"]
        current_color = self.cget("bg")
        next_color = colors[(colors.index(current_color) + 1) % len(colors)]
        self.config(bg=next_color)

# Create an instance of CustomLabel
custom_label = CustomLabel(root, text="Click me to change my color", bg="red", fg="white", font=("Arial", 16))
custom_label.pack(pady=50)
```

### 4. 📑 **Complete Code**

Here's the complete code demonstrating how to create and use a custom widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Custom Widgets Demo')

class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.change_color)

    def change_color(self, event):
        colors = ["red", "green", "blue", "yellow", "pink"]
        current_color = self.cget("bg")
        next_color = colors[(colors.index(current_color) + 1) % len(colors)]
        self.config(bg=next_color)

# Create an instance of CustomLabel
custom_label = CustomLabel(root, text="Click me to change my color", bg="red", fg="white", font=("Arial", 16))
custom_label.pack(pady=50)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `custom_widgets.py` and run it using the Python interpreter:

```sh
python custom_widgets.py
```

You should see a window with a custom label that changes color when clicked.

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
