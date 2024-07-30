# Listbox Widget 📋

Learn how to display a list of single-line text items on a Listbox in Tkinter. The Listbox widget allows users to select one or more items from a list of choices.

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
root.title("Listbox Widget Example")
```

### 3. 📋 **Creating a Listbox Widget**

You can create a Listbox widget using the `Listbox` class.

```python
# Create a Listbox widget
listbox = tk.Listbox(root, height=10)
listbox.pack(padx=10, pady=10)

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)
```

### 4. 🔄 **Retrieving the Selected Item**

You can retrieve the selected item using the `curselection` method of the Listbox.

```python
def show_selected_item():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected Item(s):", selected_items)

# Create a Button to show the selected item
button = ttk.Button(root, text="Show Selected Item", command=show_selected_item)
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Listbox widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Listbox Widget Example")

# Create and pack a Listbox widget
listbox = tk.Listbox(root, height=10)
listbox.pack(padx=10, pady=10)

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Function to show the selected item
def show_selected_item():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected Item(s):", selected_items)

# Create and pack a Button to show the selected item
button = ttk.Button(root, text="Show Selected Item", command=show_selected_item)
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `listbox_widget.py` and run it using the Python interpreter:

```sh
python listbox_widget.py
```

You should see a window with a Listbox widget allowing you to select one or more items, and a button to show the selected item(s).

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
