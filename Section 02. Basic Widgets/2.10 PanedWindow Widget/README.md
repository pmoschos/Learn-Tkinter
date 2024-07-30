# PanedWindow Widget 🪟

Learn how to use the PanedWindow to divide the space of a frame or a window in Tkinter. The PanedWindow widget allows you to add multiple resizable panes to your application.

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
root.title("PanedWindow Widget Example")
```

### 3. 🪟 **Creating a PanedWindow Widget**

You can create a PanedWindow widget using the `PanedWindow` class.

```python
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)
```

### 4. ➕ **Adding Panes to the PanedWindow**

You can add panes to the PanedWindow using the `add` method.

```python
left_frame = ttk.Frame(paned_window, width=100, height=300, relief=tk.SUNKEN)
paned_window.add(left_frame)

right_frame = ttk.Frame(paned_window, width=400, height=300, relief=tk.SUNKEN)
paned_window.add(right_frame)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the PanedWindow widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("PanedWindow Widget Example")

# Create and pack a PanedWindow widget
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Add panes to the PanedWindow
left_frame = ttk.Frame(paned_window, width=100, height=300, relief=tk.SUNKEN)
paned_window.add(left_frame)

right_frame = ttk.Frame(paned_window, width=400, height=300, relief=tk.SUNKEN)
paned_window.add(right_frame)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `panedwindow_widget.py` and run it using the Python interpreter:

```sh
python panedwindow_widget.py
```

You should see a window with a PanedWindow widget allowing you to divide the space into resizable panes.

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
