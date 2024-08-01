# Full OOP Applications 🛠️

Learn how to develop a full Tkinter object-oriented application. Using an object-oriented approach helps in organizing the code better, making it more modular and reusable.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🛠️ **Defining the Main Application Class**

You can define the main application class by creating a class that inherits from `tk.Tk`.

### Example: Main Application

Here's an example of defining the main application using an object-oriented approach:

```python
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('600x400')
        self.title('Full OOP Application Demo')

        # Create and pack frames
        self.frame1 = CustomFrame1(self)
        self.frame1.pack(side='left', expand=True, fill='both')

        self.frame2 = CustomFrame2(self)
        self.frame2.pack(side='right', expand=True, fill='both')
```

### 3. 🛠️ **Defining Custom Frames**

Define custom frames that will be used in the main application.

### Example: Custom Frames

```python
class CustomFrame1(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add a label
        self.label = ttk.Label(self, text="Frame 1")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button in Frame 1 clicked!")

class CustomFrame2(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add a label
        self.label = ttk.Label(self, text="Frame 2")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button in Frame 2 clicked!")
```

### 4. 🛠️ **Running the Application**

Create an instance of the main application class and run the application.

```python
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to develop a full Tkinter object-oriented application:

```python
import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('600x400')
        self.title('Full OOP Application Demo')

        # Create and pack frames
        self.frame1 = CustomFrame1(self)
        self.frame1.pack(side='left', expand=True, fill='both')

        self.frame2 = CustomFrame2(self)
        self.frame2.pack(side='right', expand=True, fill='both')

class CustomFrame1(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add a label
        self.label = ttk.Label(self, text="Frame 1")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button in Frame 1 clicked!")

class CustomFrame2(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add a label
        self.label = ttk.Label(self, text="Frame 2")
        self.label.pack(pady=20)

        # Add a button
        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button in Frame 2 clicked!")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

## Running the Code

Save your code in a file named `oop_applications.py` and run it using the Python interpreter:

```sh
python oop_applications.py
```

You should see a window with two custom frames, each containing a label and a button. Clicking the buttons will print messages to the console.

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
