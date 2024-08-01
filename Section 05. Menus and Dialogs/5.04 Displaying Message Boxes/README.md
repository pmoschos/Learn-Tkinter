# Displaying Message Boxes 📬

Learn how to display various message boxes such as information, warning, and error message boxes in Tkinter. The message boxes are useful for providing feedback and alerting users to specific situations.

## Getting Started

First, make sure to import Tkinter and the `messagebox` module.

### 1. 📦 **Importing Tkinter and the messagebox module**

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Displaying Message Boxes Demo')
```

### 3. 📬 **Displaying Information Message Box**

You can display an information message box using the `messagebox.showinfo` method.

```python
# Function to display an information message box
def show_info():
    messagebox.showinfo("Information", "This is an information message box.")

# Create a button to trigger the information message box
info_button = ttk.Button(root, text="Show Info", command=show_info)
info_button.pack(pady=10)
```

### 4. 📬 **Displaying Warning Message Box**

You can display a warning message box using the `messagebox.showwarning` method.

```python
# Function to display a warning message box
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message box.")

# Create a button to trigger the warning message box
warning_button = ttk.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=10)
```

### 5. 📬 **Displaying Error Message Box**

You can display an error message box using the `messagebox.showerror` method.

```python
# Function to display an error message box
def show_error():
    messagebox.showerror("Error", "This is an error message box.")

# Create a button to trigger the error message box
error_button = ttk.Button(root, text="Show Error", command=show_error)
error_button.pack(pady=10)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating how to display various message boxes:

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Displaying Message Boxes Demo')

# Function to display an information message box
def show_info():
    messagebox.showinfo("Information", "This is an information message box.")

# Create a button to trigger the information message box
info_button = ttk.Button(root, text="Show Info", command=show_info)
info_button.pack(pady=10)

# Function to display a warning message box
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message box.")

# Create a button to trigger the warning message box
warning_button = ttk.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=10)

# Function to display an error message box
def show_error():
    messagebox.showerror("Error", "This is an error message box.")

# Create a button to trigger the error message box
error_button = ttk.Button(root, text="Show Error", command=show_error)
error_button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `displaying_message_boxes.py` and run it using the Python interpreter:

```sh
python displaying_message_boxes.py
```

You should see a window with buttons that display various message boxes when clicked.

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
