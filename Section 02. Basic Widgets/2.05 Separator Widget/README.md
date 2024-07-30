# Separator Widget ➖

Learn how to use a separator widget to separate fields in Tkinter. The Separator widget is a simple widget that provides a visual separator between other widgets.

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
root.title("Separator Widget Example")
```

### 3. ➖ **Creating a Separator Widget**

You can create a Separator widget to separate other widgets.

```python
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)
```

### 4. ➕ **Adding Widgets Above and Below the Separator**

Add some widgets above and below the Separator widget to see it in action.

```python
label1 = ttk.Label(root, text="Above the separator")
label1.pack(pady=5)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

label2 = ttk.Label(root, text="Below the separator")
label2.pack(pady=5)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Separator widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Separator Widget Example")

# Add a Label widget above the Separator
label1 = ttk.Label(root, text="Above the separator")
label1.pack(pady=5)

# Create and pack a Separator widget
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

# Add a Label widget below the Separator
label2 = ttk.Label(root, text="Below the separator")
label2.pack(pady=5)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `separator_widget.py` and run it using the Python interpreter:

```sh
python separator_widget.py
```

You should see a window with a Separator widget separating two Label widgets.

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
