# Using Dialogs 🗨️

Explore various dialog boxes, including Yes/No, OK/Cancel, Retry/Cancel, and Open File dialogs in Tkinter. Dialog boxes are useful for interacting with users and gathering input or making decisions.

## Getting Started

First, make sure to import Tkinter and the `messagebox` and `filedialog` modules.

### 1. 📦 **Importing Tkinter and the messagebox and filedialog modules**

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Using Dialogs Demo')
```

### 3. 🗨️ **Displaying Yes/No Dialog**

You can display a Yes/No dialog using the `messagebox.askyesno` method.

```python
# Function to display a Yes/No dialog
def show_yes_no():
    result = messagebox.askyesno("Question", "Do you want to proceed?")
    print(f"Yes/No result: {result}")

# Create a button to trigger the Yes/No dialog
yes_no_button = ttk.Button(root, text="Show Yes/No", command=show_yes_no)
yes_no_button.pack(pady=10)
```

### 4. 🗨️ **Displaying OK/Cancel Dialog**

You can display an OK/Cancel dialog using the `messagebox.askokcancel` method.

```python
# Function to display an OK/Cancel dialog
def show_ok_cancel():
    result = messagebox.askokcancel("Question", "Do you want to save changes?")
    print(f"OK/Cancel result: {result}")

# Create a button to trigger the OK/Cancel dialog
ok_cancel_button = ttk.Button(root, text="Show OK/Cancel", command=show_ok_cancel)
ok_cancel_button.pack(pady=10)
```

### 5. 🗨️ **Displaying Retry/Cancel Dialog**

You can display a Retry/Cancel dialog using the `messagebox.askretrycancel` method.

```python
# Function to display a Retry/Cancel dialog
def show_retry_cancel():
    result = messagebox.askretrycancel("Question", "Do you want to retry the operation?")
    print(f"Retry/Cancel result: {result}")

# Create a button to trigger the Retry/Cancel dialog
retry_cancel_button = ttk.Button(root, text="Show Retry/Cancel", command=show_retry_cancel)
retry_cancel_button.pack(pady=10)
```

### 6. 🗨️ **Displaying Open File Dialog**

You can display an Open File dialog using the `filedialog.askopenfilename` method.

```python
# Function to display an Open File dialog
def show_open_file():
    file_path = filedialog.askopenfilename(title="Open File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    print(f"Selected file: {file_path}")

# Create a button to trigger the Open File dialog
open_file_button = ttk.Button(root, text="Open File", command=show_open_file)
open_file_button.pack(pady=10)
```

### 7. 📑 **Complete Code**

Here's the complete code demonstrating how to use various dialogs:

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Using Dialogs Demo')

# Function to display a Yes/No dialog
def show_yes_no():
    result = messagebox.askyesno("Question", "Do you want to proceed?")
    print(f"Yes/No result: {result}")

# Create a button to trigger the Yes/No dialog
yes_no_button = ttk.Button(root, text="Show Yes/No", command=show_yes_no)
yes_no_button.pack(pady=10)

# Function to display an OK/Cancel dialog
def show_ok_cancel():
    result = messagebox.askokcancel("Question", "Do you want to save changes?")
    print(f"OK/Cancel result: {result}")

# Create a button to trigger the OK/Cancel dialog
ok_cancel_button = ttk.Button(root, text="Show OK/Cancel", command=show_ok_cancel)
ok_cancel_button.pack(pady=10)

# Function to display a Retry/Cancel dialog
def show_retry_cancel():
    result = messagebox.askretrycancel("Question", "Do you want to retry the operation?")
    print(f"Retry/Cancel result: {result}")

# Create a button to trigger the Retry/Cancel dialog
retry_cancel_button = ttk.Button(root, text="Show Retry/Cancel", command=show_retry_cancel)
retry_cancel_button.pack(pady=10)

# Function to display an Open File dialog
def show_open_file():
    file_path = filedialog.askopenfilename(title="Open File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    print(f"Selected file: {file_path}")

# Create a button to trigger the Open File dialog
open_file_button = ttk.Button(root, text="Open File", command=show_open_file)
open_file_button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `using_dialogs.py` and run it using the Python interpreter:

```sh
python using_dialogs.py
```

You should see a window with buttons that display various dialogs when clicked.

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
