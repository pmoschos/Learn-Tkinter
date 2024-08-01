# Treeview Widget 🌳

Learn how to create Treeview widgets that display tabular and hierarchical data in Tkinter. The Treeview widget allows you to create hierarchical structures and tabular data representations.

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
root.geometry('600x400')
root.title('Treeview Demo')
```

### 3. 🌳 **Creating a Treeview Widget**

You can create a Treeview widget using the `Treeview` class.

```python
# Create a Treeview widget
tree = ttk.Treeview(root)
tree.pack(pady=20, fill='both', expand=True)
```

### 4. ➕ **Adding Columns to the Treeview**

You can add columns to the Treeview to display tabular data.

```python
# Define columns
tree['columns'] = ('Name', 'Age', 'Email')

# Format columns
tree.column('#0', width=0, stretch=tk.NO)
tree.column('Name', anchor=tk.W, width=120)
tree.column('Age', anchor=tk.CENTER, width=80)
tree.column('Email', anchor=tk.W, width=200)

# Create headings
tree.heading('#0', text='', anchor=tk.W)
tree.heading('Name', text='Name', anchor=tk.W)
tree.heading('Age', text='Age', anchor=tk.CENTER)
tree.heading('Email', text='Email', anchor=tk.W)
```

### 5. ➕ **Adding Data to the Treeview**

You can add data to the Treeview using the `insert` method.

```python
# Add data
tree.insert(parent='', index='end', iid=0, text='', values=('John Doe', '30', 'john.doe@example.com'))
tree.insert(parent='', index='end', iid=1, text='', values=('Jane Smith', '25', 'jane.smith@example.com'))
tree.insert(parent='', index='end', iid=2, text='', values=('Mike Johnson', '40', 'mike.johnson@example.com'))
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Treeview widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('600x400')
root.title('Treeview Demo')

# Create a Treeview widget
tree = ttk.Treeview(root)
tree.pack(pady=20, fill='both', expand=True)

# Define columns
tree['columns'] = ('Name', 'Age', 'Email')

# Format columns
tree.column('#0', width=0, stretch=tk.NO)
tree.column('Name', anchor=tk.W, width=120)
tree.column('Age', anchor=tk.CENTER, width=80)
tree.column('Email', anchor=tk.W, width=200)

# Create headings
tree.heading('#0', text='', anchor=tk.W)
tree.heading('Name', text='Name', anchor=tk.W)
tree.heading('Age', text='Age', anchor=tk.CENTER)
tree.heading('Email', text='Email', anchor=tk.W)

# Add data
tree.insert(parent='', index='end', iid=0, text='', values=('John Doe', '30', 'john.doe@example.com'))
tree.insert(parent='', index='end', iid=1, text='', values=('Jane Smith', '25', 'jane.smith@example.com'))
tree.insert(parent='', index='end', iid=2, text='', values=('Mike Johnson', '40', 'mike.johnson@example.com'))

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `treeview_widget.py` and run it using the Python interpreter:

```sh
python treeview_widget.py
```

You should see a window with a Treeview widget displaying tabular data with three columns.

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
