# Radio Button Widget 🔘

Learn how to use radio buttons to allow users to select one of several mutually exclusive choices in Tkinter. The Radio Button widget is a standard widget used to implement this kind of choice selection.

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
root.title("Radio Button Widget Example")
```

### 3. 🔘 **Creating Radio Button Widgets**

You can create Radio Button widgets using the `Radiobutton` class. All radio buttons in a group should share the same variable.

```python
# Variable to store the state of the selected radio button
selected_option = tk.StringVar(value="Option 1")

# Create Radio Button widgets
radio1 = ttk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1")
radio2 = ttk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2")
radio3 = ttk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3")

# Pack the Radio Button widgets
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)
```

### 4. 🔄 **Retrieving the Selected Option**

You can retrieve the state of the selected radio button using the `get` method of the variable.

```python
def show_selected_option():
    print("Selected Option:", selected_option.get())

# Create a Button to show the selected option
button = ttk.Button(root, text="Show Selected Option", command=show_selected_option)
button.pack(pady=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Radio Button widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Radio Button Widget Example")

# Variable to store the state of the selected radio button
selected_option = tk.StringVar(value="Option 1")

# Create and pack Radio Button widgets
radio1 = ttk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1")
radio2 = ttk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2")
radio3 = ttk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3")

radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Function to show the selected option
def show_selected_option():
    print("Selected Option:", selected_option.get())

# Create and pack a Button to show the selected option
button = ttk.Button(root, text="Show Selected Option", command=show_selected_option)
button.pack(pady=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `radiobutton_widget.py` and run it using the Python interpreter:

```sh
python radiobutton_widget.py
```

You should see a window with Radio Button widgets allowing you to select one of several options, and a button to show the selected option.

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
