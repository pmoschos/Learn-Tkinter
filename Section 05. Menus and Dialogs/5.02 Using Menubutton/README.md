# Using Menubutton 🔽

Learn how to use the Menubutton widget in Tkinter. The Menubutton widget allows you to create a button that displays a menu when clicked.

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
root.title('Using Menubutton Demo')
```

### 3. 🔽 **Creating a Menubutton**

You can create a Menubutton widget using the `Menubutton` class and attach a menu to it.

```python
# Create a Menubutton
menubutton = ttk.Menubutton(root, text='Options')
menubutton.pack(pady=20)

# Create a Menu and attach it to the Menubutton
menu = tk.Menu(menubutton, tearoff=0)
menubutton['menu'] = menu

# Add menu items to the Menu
menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
menu.add_command(label="Option 3", command=lambda: print("Option 3 selected"))
```

### 4. 📑 **Complete Code**

Here's the complete code demonstrating how to use the Menubutton widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Using Menubutton Demo')

# Create a Menubutton
menubutton = ttk.Menubutton(root, text='Options')
menubutton.pack(pady=20)

# Create a Menu and attach it to the Menubutton
menu = tk.Menu(menubutton, tearoff=0)
menubutton['menu'] = menu

# Add menu items to the Menu
menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
menu.add_command(label="Option 3", command=lambda: print("Option 3 selected"))

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `using_menubutton.py` and run it using the Python interpreter:

```sh
python using_menubutton.py
```

You should see a window with a Menubutton that displays a menu with options when clicked.

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
