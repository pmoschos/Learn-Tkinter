# Switching Between Frames 🔄

Learn how to switch between frames in a Tkinter application. This guide covers how to create multiple frames and switch between them using an object-oriented approach.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🔄 **Defining the Main Application Class**

You can define the main application class by creating a class that inherits from `tk.Tk`.

### Example: Main Application

Here's an example of defining the main application using an object-oriented approach:

```python
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('600x400')
        self.title('Switching Frames Demo')

        # Create a container for the frames
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Create a dictionary to hold the frames
        self.frames = {}

        # Add frames to the dictionary
        for F in (Frame1, Frame2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Frame1")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
```

### 3. 🔄 **Defining Custom Frames**

Define custom frames that will be used in the main application.

### Example: Custom Frames

```python
class Frame1(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        # Add a label
        self.label = ttk.Label(self, text="This is Frame 1")
        self.label.pack(pady=20)

        # Add a button to switch to Frame 2
        self.button = ttk.Button(self, text="Go to Frame 2", command=lambda: controller.show_frame("Frame2"))
        self.button.pack(pady=10)

class Frame2(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        # Add a label
        self.label = ttk.Label(self, text="This is Frame 2")
        self.label.pack(pady=20)

        # Add a button to switch to Frame 1
        self.button = ttk.Button(self, text="Go to Frame 1", command=lambda: controller.show_frame("Frame1"))
        self.button.pack(pady=10)
```

### 4. 🔄 **Running the Application**

Create an instance of the main application class and run the application.

```python
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to switch between frames in a Tkinter application:

```python
import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('600x400')
        self.title('Switching Frames Demo')

        # Create a container for the frames
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Create a dictionary to hold the frames
        self.frames = {}

        # Add frames to the dictionary
        for F in (Frame1, Frame2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Frame1")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Frame1(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        # Add a label
        self.label = ttk.Label(self, text="This is Frame 1")
        self.label.pack(pady=20)

        # Add a button to switch to Frame 2
        self.button = ttk.Button(self, text="Go to Frame 2", command=lambda: controller.show_frame("Frame2"))
        self.button.pack(pady=10)

class Frame2(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        # Add a label
        self.label = ttk.Label(self, text="This is Frame 2")
        self.label.pack(pady=20)

        # Add a button to switch to Frame 1
        self.button = ttk.Button(self, text="Go to Frame 1", command=lambda: controller.show_frame("Frame1"))
        self.button.pack(pady=10)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
```

## Running the Code

Save your code in a file named `switching_frames.py` and run it using the Python interpreter:

```sh
python switching_frames.py
```

You should see a window with two frames that can be switched between using the buttons.

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
