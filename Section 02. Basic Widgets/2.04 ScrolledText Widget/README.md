# ScrolledText Widget 📝

Learn how to create a scrolled text widget that consists of Text and vertical scrollbar widgets in Tkinter. The ScrolledText widget provides a convenient way to have a text area with a built-in vertical scrollbar.

## Getting Started

First, make sure to import Tkinter and ScrolledText.

### 1. 📦 **Importing Tkinter and ScrolledText**

```python
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.title("ScrolledText Widget Example")
```

### 3. 📝 **Creating a ScrolledText Widget**

You can create a ScrolledText widget to allow multi-line text input with a built-in scrollbar.

```python
scrolled_text = ScrolledText(root, width=40, height=10, wrap='word')
scrolled_text.pack(padx=10, pady=10)
```

### 4. 🔄 **Adding Content to the ScrolledText Widget**

Add some content to the ScrolledText widget to see the scrollbar in action.

```python
sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""

scrolled_text.insert('1.0', sample_text)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the ScrolledText widget:

```python
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Create the main window
root = tk.Tk()
root.title("ScrolledText Widget Example")

# Create and pack a ScrolledText widget
scrolled_text = ScrolledText(root, width=40, height=10, wrap='word')
scrolled_text.pack(padx=10, pady=10)

# Add content to the ScrolledText widget
sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""

scrolled_text.insert('1.0', sample_text)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `scrolledtext_widget.py` and run it using the Python interpreter:

```sh
python scrolledtext_widget.py
```

You should see a window with a ScrolledText widget allowing you to navigate through the text content.

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
