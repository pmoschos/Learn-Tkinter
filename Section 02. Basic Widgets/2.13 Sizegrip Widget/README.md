# Sizegrip Widget ↔️

Learn how to use the Sizegrip widget to allow users to resize the entire application window in Tkinter. The Sizegrip widget provides a small control in the corner of the window that users can drag to resize the window.

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
root.title("Sizegrip Widget Example")
root.geometry("300x200")
```

### 3. ↔️ **Creating a Sizegrip Widget**

You can create a Sizegrip widget using the `Sizegrip` class and pack it to the bottom-right corner of the window.

```python
# Create a Sizegrip widget
sizegrip = ttk.Sizegrip(root)
sizegrip.pack(side="right", anchor="se")
```

### 4. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Sizegrip widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Sizegrip Widget Example")
root.geometry("300x200")

# Create and pack a Sizegrip widget
sizegrip = ttk.Sizegrip(root)
sizegrip.pack(side="right", anchor="se")

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `sizegrip_widget.py` and run it using the Python interpreter:

```sh
python sizegrip_widget.py
```

You should see a window with a Sizegrip widget in the bottom-right corner allowing you to resize the window.

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
