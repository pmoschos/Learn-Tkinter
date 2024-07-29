# Hello, Tkinter! 🌟

Welcome to your first Tkinter program! This guide will walk you through creating a simple "Hello, World!" application using Tkinter, Python's standard GUI (Graphical User Interface) toolkit.

## Getting Started

Tkinter is included with standard distributions of Python, so there's no need to install anything extra. Let's get started with the basics!

### 1. 📦 **Importing Tkinter**

To use Tkinter, you need to import it. The common practice is to import Tkinter with an alias `tk`.

```python
import tkinter as tk
```

### 2. 🖼️ **Creating the Main Window**

The main window, or root window, is where your application will run. It's created by initializing the `Tk` class.

```python
# Create the main window
root = tk.Tk()
```

### 3. 📝 **Adding a Label**

A Label widget is used to display text or images. For our "Hello, World!" program, we'll use it to display text.

```python
# Create a Label widget
label = tk.Label(root, text="Hello, World!")
```

### 4. 📐 **Packing the Widget**

The `pack` method is a geometry manager that organizes widgets in blocks before placing them in the parent widget.

```python
# Pack the Label widget
label.pack()
```

### 5. ▶️ **Running the Application**

To run the Tkinter event loop, use the `mainloop` method. This will keep your application running until you close the window.

```python
# Run the application
root.mainloop()
```

## Complete Code

Here's the complete code for your first Tkinter program:

```python
import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a Label widget
label = tk.Label(root, text="Hello, World!")

# Pack the Label widget
label.pack()

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `hello_tkinter.py` and run it using the Python interpreter:

```sh
python hello_tkinter.py
```

You should see a window displaying "Hello, World!".

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
