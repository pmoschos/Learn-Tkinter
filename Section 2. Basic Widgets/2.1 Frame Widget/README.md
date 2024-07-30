# Frame Widget 📋

Learn how to use the Frame widget to group other widgets in Tkinter. The Frame widget is a versatile container widget that can hold other widgets, making it easier to organize your application's layout.

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
root.title("Frame Widget Example")
```

### 3. 📋 **Creating a Frame**

You can create a Frame widget to group other widgets.

```python
frame = ttk.Frame(root, padding="10")
frame.pack(padx=10, pady=10, fill='x', expand=True)
```

### 4. ➕ **Adding Widgets to the Frame**

Add widgets to the Frame just like you would add them to the main window.

```python
label = ttk.Label(frame, text="This is a label inside a frame.")
label.pack(pady=5)

button = ttk.Button(frame, text="Click Me")
button.pack(pady=5)
```

### 5. 🔄 **Configuring the Frame**

You can configure the Frame to adjust its appearance and behavior.

```python
frame.config(relief='sunken', borderwidth=2)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Frame widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Frame Widget Example")

# Create and pack a Frame widget
frame = ttk.Frame(root, padding="10")
frame.pack(padx=10, pady=10, fill='x', expand=True)

# Add a Label widget to the Frame
label = ttk.Label(frame, text="This is a label inside a frame.")
label.pack(pady=5)

# Add a Button widget to the Frame
button = ttk.Button(frame, text="Click Me")
button.pack(pady=5)

# Configure the Frame
frame.config(relief='sunken', borderwidth=2)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `frame_widget.py` and run it using the Python interpreter:

```sh
python frame_widget.py
```

You should see a window with a Frame containing a label and a button.

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
