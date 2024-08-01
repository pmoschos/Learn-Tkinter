# Handling User Input 💬

Explore techniques for handling user input in your Tkinter applications. This guide covers various widgets and methods to capture and process user input effectively.

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
root.title('Handling User Input Demo')
```

### 3. 💬 **Capturing Text Input**

You can use the `Entry` widget to capture single-line text input.

```python
# Function to handle the input
def handle_text_input():
    user_input = entry.get()
    print(f"User input: {user_input}")

# Create an entry widget and a button to capture the input
entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

button = ttk.Button(root, text='Submit', command=handle_text_input)
button.pack(pady=10)
```

### 4. 💬 **Capturing Multi-line Text Input**

You can use the `Text` widget to capture multi-line text input.

```python
# Function to handle the multi-line input
def handle_multiline_input():
    user_input = text.get("1.0", tk.END).strip()
    print(f"User input: {user_input}")

# Create a text widget and a button to capture the input
text = tk.Text(root, width=30, height=5)
text.pack(pady=10)

button_multiline = ttk.Button(root, text='Submit Multi-line', command=handle_multiline_input)
button_multiline.pack(pady=10)
```

### 5. 💬 **Capturing Selection Input**

You can use the `Combobox` and `Radiobutton` widgets to capture selection input.

```python
# Function to handle combobox selection
def handle_combobox_selection(event):
    selected_item = combobox.get()
    print(f"Selected item: {selected_item}")

# Create a combobox widget
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(pady=10)
combobox.bind("<<ComboboxSelected>>", handle_combobox_selection)

# Function to handle radio button selection
def handle_radiobutton_selection():
    selected_option = radio_var.get()
    print(f"Selected option: {selected_option}")

# Create radio buttons
radio_var = tk.StringVar(value="Option 1")
radio1 = ttk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=handle_radiobutton_selection)
radio2 = ttk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=handle_radiobutton_selection)
radio3 = ttk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3", command=handle_radiobutton_selection)

radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating how to handle user input:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Handling User Input Demo')

# Function to handle the input
def handle_text_input():
    user_input = entry.get()
    print(f"User input: {user_input}")

# Create an entry widget and a button to capture the input
entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

button = ttk.Button(root, text='Submit', command=handle_text_input)
button.pack(pady=10)

# Function to handle the multi-line input
def handle_multiline_input():
    user_input = text.get("1.0", tk.END).strip()
    print(f"User input: {user_input}")

# Create a text widget and a button to capture the input
text = tk.Text(root, width=30, height=5)
text.pack(pady=10)

button_multiline = ttk.Button(root, text='Submit Multi-line', command=handle_multiline_input)
button_multiline.pack(pady=10)

# Function to handle combobox selection
def handle_combobox_selection(event):
    selected_item = combobox.get()
    print(f"Selected item: {selected_item}")

# Create a combobox widget
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(pady=10)
combobox.bind("<<ComboboxSelected>>", handle_combobox_selection)

# Function to handle radio button selection
def handle_radiobutton_selection():
    selected_option = radio_var.get()
    print(f"Selected option: {selected_option}")

# Create radio buttons
radio_var = tk.StringVar(value="Option 1")
radio1 = ttk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=handle_radiobutton_selection)
radio2 = ttk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=handle_radiobutton_selection)
radio3 = ttk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3", command=handle_radiobutton_selection)

radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `handling_user_input.py` and run it using the Python interpreter:

```sh
python handling_user_input.py
```

You should see a window demonstrating various techniques for handling user input.

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
