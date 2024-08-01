# Notebook Widget 📓

Learn how to use the Notebook widget to create tabs in Tkinter. The Notebook widget allows you to create tabbed interfaces, which is useful for organizing content into multiple sections.

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
root.title('Notebook Demo')
```

### 3. 📓 **Creating a Notebook Widget**

You can create a Notebook widget using the `Notebook` class.

```python
# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky='nsew')
```

### 4. ➕ **Adding Frames to the Notebook**

You can add frames to the Notebook and then add the frames to the Notebook using the `add` method.

```python
# Create frames
home_frame = ttk.Frame(notebook, width=400, height=280)
settings_frame = ttk.Frame(notebook, width=400, height=280)
profile_frame = ttk.Frame(notebook, width=400, height=280)
about_frame = ttk.Frame(notebook, width=400, height=280)

# Add frames to notebook
notebook.add(home_frame, text='Home')
notebook.add(settings_frame, text='Settings')
notebook.add(profile_frame, text='Profile')
notebook.add(about_frame, text='About')
```

### 5. ➕ **Adding Content to the Tabs**

You can add content to the tabs using standard Tkinter widgets.

```python
# Add content to the tabs
ttk.Label(home_frame, text="Welcome to the Home tab").pack(pady=10, padx=10)
ttk.Label(settings_frame, text="Adjust your settings here").pack(pady=10, padx=10)
ttk.Label(profile_frame, text="User Profile Information").pack(pady=10, padx=10)
ttk.Label(about_frame, text="About this application").pack(pady=10, padx=10)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Notebook widget:

```python
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky='nsew')

# create frames
home_frame = ttk.Frame(notebook, width=400, height=280)
settings_frame = ttk.Frame(notebook, width=400, height=280)
profile_frame = ttk.Frame(notebook, width=400, height=280)
about_frame = ttk.Frame(notebook, width=400, height=280)

# add frames to notebook
notebook.add(home_frame, text='Home')
notebook.add(settings_frame, text='Settings')
notebook.add(profile_frame, text='Profile')
notebook.add(about_frame, text='About')

# add content to the tabs
ttk.Label(home_frame, text="Welcome to the Home tab").pack(pady=10, padx=10)
ttk.Label(settings_frame, text="Adjust your settings here").pack(pady=10, padx=10)
ttk.Label(profile_frame, text="User Profile Information").pack(pady=10, padx=10)
ttk.Label(about_frame, text="About this application").pack(pady=10, padx=10)

# Configure the grid to expand properly
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
```

## Running the Code

Save your code in a file named `notebook_widget.py` and run it using the Python interpreter:

```sh
python notebook_widget.py
```

You should see a window with a Notebook widget containing four tabs, each with its own content.

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
