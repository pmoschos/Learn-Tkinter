# Creating Menus 🍽️

Learn how to add a menu bar and menus to a window in Tkinter. This guide covers how to create and configure menu bars, menus, and menu items.

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
root.geometry('400x300')
root.title('Creating Menus Demo')
```

### 3. 🍽️ **Creating a Menu Bar**

You can create a menu bar using the `Menu` class and attach it to the main window.

```python
# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
```

### 4. 🍽️ **Adding Menus to the Menu Bar**

You can add menus to the menu bar and add menu items to the menus.

```python
# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu items to the File menu
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_command(label="Save", command=lambda: print("Save File"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
```

### 5. 🍽️ **Adding More Menus**

You can add more menus to the menu bar in a similar way.

```python
# Create an Edit menu and add it to the menu bar
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add menu items to the Edit menu
edit_menu.add_command(label="Cut", command=lambda: print("Cut"))
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))

# Create a Help menu and add it to the menu bar
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add menu items to the Help menu
help_menu.add_command(label="About", command=lambda: print("About"))
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating how to create menus:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Creating Menus Demo')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu items to the File menu
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_command(label="Save", command=lambda: print("Save File"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an Edit menu and add it to the menu bar
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add menu items to the Edit menu
edit_menu.add_command(label="Cut", command=lambda: print("Cut"))
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))

# Create a Help menu and add it to the menu bar
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add menu items to the Help menu
help_menu.add_command(label="About", command=lambda: print("About"))

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `creating_menus.py` and run it using the Python interpreter:

```sh
python creating_menus.py
```

You should see a window with a menu bar containing File, Edit, and Help menus with their respective menu items.

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
