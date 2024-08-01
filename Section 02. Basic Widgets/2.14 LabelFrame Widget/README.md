# LabelFrame Widget 🏷️

Learn how to group related widgets in a group using the LabelFrame widget in Tkinter. The LabelFrame widget is a container widget that can be used to group related widgets with a border and a title.

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
root.title("LabelFrame Widget Example")
```

### 3. 🏷️ **Creating a LabelFrame Widget**

You can create a LabelFrame widget using the `LabelFrame` class.

```python
# Create a LabelFrame widget
labelframe = ttk.LabelFrame(root, text="User Information", padding=(10, 10))
labelframe.pack(padx=10, pady=10, fill="both", expand=True)
```

### 4. ➕ **Adding Widgets to the LabelFrame**

Add widgets to the LabelFrame just like you would add them to the main window.

```python
# Add widgets to the LabelFrame
name_label = ttk.Label(labelframe, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

name_entry = ttk.Entry(labelframe)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

email_label = ttk.Label(labelframe, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

email_entry = ttk.Entry(labelframe)
email_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Configure grid weights for the LabelFrame
labelframe.columnconfigure(1, weight=1)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the LabelFrame widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("LabelFrame Widget Example")

# Create and pack a LabelFrame widget
labelframe = ttk.LabelFrame(root, text="User Information", padding=(10, 10))
labelframe.pack(padx=10, pady=10, fill="both", expand=True)

# Add widgets to the LabelFrame
name_label = ttk.Label(labelframe, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

name_entry = ttk.Entry(labelframe)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

email_label = ttk.Label(labelframe, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

email_entry = ttk.Entry(labelframe)
email_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Configure grid weights for the LabelFrame
labelframe.columnconfigure(1, weight=1)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `labelframe_widget.py` and run it using the Python interpreter:

```sh
python labelframe_widget.py
```

You should see a window with a LabelFrame widget containing a group of related widgets.

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
