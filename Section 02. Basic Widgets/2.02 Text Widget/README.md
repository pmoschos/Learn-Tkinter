# Text Widget 📝

Learn how to create and use a multi-line text input field in Tkinter. The Text widget is a versatile widget that allows users to enter and edit multi-line text.

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
root.title("Text Widget Example")
```

### 3. 📝 **Creating a Text Widget**

You can create a Text widget to allow multi-line text input.

```python
text = tk.Text(root, width=40, height=10)
text.pack(padx=10, pady=10)
```

### 4. 🔄 **Configuring the Text Widget**

You can configure the Text widget to adjust its appearance and behavior.

```python
text.config(wrap='word', font=("Helvetica", 12))
```

### 5. ➕ **Adding Scrollbars**

You can add scrollbars to the Text widget to handle large amounts of text.

```python
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y')
text.config(yscrollcommand=scrollbar.set)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Text widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Text Widget Example")

# Create and pack a Text widget
text = tk.Text(root, width=40, height=10)
text.pack(padx=10, pady=10)

# Configure the Text widget
text.config(wrap='word', font=("Helvetica", 12))

# Add a vertical scrollbar to the Text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y')
text.config(yscrollcommand=scrollbar.set)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `text_widget.py` and run it using the Python interpreter:

```sh
python text_widget.py
```

You should see a window with a multi-line text input field and a scrollbar.

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
