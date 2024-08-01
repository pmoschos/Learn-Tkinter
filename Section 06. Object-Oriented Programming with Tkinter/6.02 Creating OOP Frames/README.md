# Creating OOP Frames 🖼️

Learn how to define an object-oriented Frame in Tkinter. Using an object-oriented approach for frames helps in organizing the code better, making it more modular and reusable.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🖼️ **Defining an Object-Oriented Frame Class**

You can define an object-oriented frame by creating a class that inherits from `tk.Frame` or `ttk.Frame`.

### Example: Custom Frame

Here's an example of defining a custom frame using an object-oriented approach:

```python
class CustomFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add a label
        self.label = ttk.Label(self, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button clicked!")
```

### 3. 🖼️ **Using the Custom Frame in a Window**

Create an instance of the custom frame and add it to the main window.

```python
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('400x300')
        self.title('OOP Frames Demo')

        # Create an instance of CustomFrame
        self.frame = CustomFrame(self)
        self.frame.pack(expand=True, fill='both')

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

### 4. 📑 **Complete Code**

Here's the complete code demonstrating how to define an object-oriented frame and use it in a window:

```python
import tkinter as tk
from tkinter import ttk

class CustomFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add a label
        self.label = ttk.Label(self, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button clicked!")

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('400x300')
        self.title('OOP Frames Demo')

        # Create an instance of CustomFrame
        self.frame = CustomFrame(self)
        self.frame.pack(expand=True, fill='both')

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

## Running the Code

Save your code in a file named `oop_frames.py` and run it using the Python interpreter:

```sh
python oop_frames.py
```

You should see a window with a custom frame that contains a label and a button, and clicking the button will print a message to the console.

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
