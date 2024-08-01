# Tkinter MVC Pattern 🏛️

Learn how to structure a Tkinter application using the MVC (Model-View-Controller) design pattern. This pattern helps in separating the concerns of the application, making it more modular and maintainable.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🏛️ **Defining the Model**

The model represents the data and business logic of the application.

```python
class Model:
    def __init__(self):
        self.data = "Hello, Tkinter MVC!"

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data
```

### 3. 🏛️ **Defining the View**

The view represents the UI elements of the application.

```python
class View(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = ttk.Label(self, text="")
        self.label.pack(pady=20)

        self.entry = ttk.Entry(self)
        self.entry.pack(pady=10)

        self.button = ttk.Button(self, text="Update", command=self.update_data)
        self.button.pack(pady=10)

    def update_data(self):
        new_data = self.entry.get()
        self.controller.update_model_data(new_data)

    def set_label_text(self, text):
        self.label.config(text=text)
```

### 4. 🏛️ **Defining the Controller**

The controller handles the interaction between the model and the view.

```python
class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)
        self.view.pack(expand=True, fill='both')
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        self.view.set_label_text(data)

    def update_model_data(self, new_data):
        self.model.set_data(new_data)
        self.update_view()
```

### 5. 🏛️ **Running the Application**

Create an instance of the controller and run the application.

```python
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x300')
    root.title('Tkinter MVC Pattern Demo')
    app = Controller(root)
    root.mainloop()
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating the MVC pattern in a Tkinter application:

```python
import tkinter as tk
from tkinter import ttk

class Model:
    def __init__(self):
        self.data = "Hello, Tkinter MVC!"

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

class View(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = ttk.Label(self, text="")
        self.label.pack(pady=20)

        self.entry = ttk.Entry(self)
        self.entry.pack(pady=10)

        self.button = ttk.Button(self, text="Update", command=self.update_data)
        self.button.pack(pady=10)

    def update_data(self):
        new_data = self.entry.get()
        self.controller.update_model_data(new_data)

    def set_label_text(self, text):
        self.label.config(text=text)

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)
        self.view.pack(expand=True, fill='both')
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        self.view.set_label_text(data)

    def update_model_data(self, new_data):
        self.model.set_data(new_data)
        self.update_view()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x300')
    root.title('Tkinter MVC Pattern Demo')
    app = Controller(root)
    root.mainloop()
```

## Running the Code

Save your code in a file named `mvc_pattern.py` and run it using the Python interpreter:

```sh
python mvc_pattern.py
```

You should see a window with a label, entry, and button. The label updates when you enter text and click the update button.

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
