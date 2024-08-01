# Defining OOP Windows 🏛️

Learn how to define an object-oriented window in Tkinter. Using an object-oriented approach helps in organizing the code better, making it more modular and reusable.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🏛️ **Defining an Object-Oriented Window Class**

You can define an object-oriented window by creating a class that inherits from `tk.Tk` or `tk.Toplevel`.

### Example: Main Application Window

Here's an example of defining the main application window using an object-oriented approach:

```python
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('400x300')
        self.title('OOP Windows Demo')

        # Add a label
        self.label = ttk.Label(self, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button clicked!")
```

### 3. 🏛️ **Running the Application**

Create an instance of the class and run the application.

```python
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

### 4. 📑 **Complete Code**

Here's the complete code demonstrating how to define an object-oriented window:

```python
import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('400x300')
        self.title('OOP Windows Demo')

        # Add a label
        self.label = ttk.Label(self, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

## Running the Code

Save your code in a file named `oop_windows.py` and run it using the Python interpreter:

```sh
python oop_windows.py
```

You should see a window with a label and a button, and clicking the button will print a message to the console.

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
