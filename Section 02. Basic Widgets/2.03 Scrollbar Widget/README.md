# Scrollbar Widget 📜

Learn how to link a scrollbar to a scrollable widget, such as a Text widget in Tkinter. The Scrollbar widget allows users to navigate through large amounts of content.

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
root.title("Scrollbar Widget Example")
```

### 3. 📜 **Creating a Scrollbar**

You can create a Scrollbar widget and link it to a Text widget.

```python
# Create a Text widget
text = tk.Text(root, width=40, height=10, wrap='word')
text.pack(side='left', fill='both', expand=True, padx=10, pady=10)

# Create a Scrollbar widget and link it to the Text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y')

text.config(yscrollcommand=scrollbar.set)
```

### 4. 🔄 **Adding Content to the Text Widget**

Add some content to the Text widget to see the scrollbar in action.

```python
sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""

text.insert('1.0', sample_text)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Scrollbar widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Scrollbar Widget Example")

# Create a Text widget
text = tk.Text(root, width=40, height=10, wrap='word')
text.pack(side='left', fill='both', expand=True, padx=10, pady=10)

# Create a Scrollbar widget and link it to the Text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y')

text.config(yscrollcommand=scrollbar.set)

# Add content to the Text widget
sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""

text.insert('1.0', sample_text)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `scrollbar_widget.py` and run it using the Python interpreter:

```sh
python scrollbar_widget.py
```

You should see a window with a Text widget and a scrollbar allowing you to navigate through the text content.

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
