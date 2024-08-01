# Tkinter MVC Pattern 🏛️

Learn how to structure a Tkinter application using the MVC (Model-View-Controller) design pattern. This pattern helps in separating the concerns of the application, making it more modular and maintainable.

## Getting Started

First, make sure to import Tkinter, ttk, and other necessary modules.

### 1. 📦 **Importing Tkinter, ttk, and re**

```python
import re
import tkinter as tk
from tkinter import ttk
```

### 2. 🏛️ **Defining the Model**

The model represents the data and business logic of the application.

```python
class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')
```

### 3. 🏛️ **Defining the View**

The view represents the UI elements of the application.

```python
class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        self.message_label['text'] = ''
```

### 4. 🏛️ **Defining the Controller**

The controller handles the interaction between the model and the view.

```python
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        try:
            self.model.email = email
            self.model.save()
            self.view.show_success(f'The email {email} saved!')
        except ValueError as error:
            self.view.show_error(error)
```

### 5. 🏛️ **Running the Application**

Create an instance of the application and run it.

```python
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        model = Model('hello@pythontutorial.net')

        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        controller = Controller(model, view)

        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating the MVC pattern in a Tkinter application:

```python
import re
import tkinter as tk
from tkinter import ttk

class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        self.message_label['text'] = ''

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        try:
            self.model.email = email
            self.model.save()
            self.view.show_success(f'The email {email} saved!')
        except ValueError as error:
            self.view.show_error(error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        model = Model('hello@pythontutorial.net')

        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        controller = Controller(model, view)

        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
```

## Running the Code

Save your code in a file named `mvc_pattern.py` and run it using the Python interpreter:

```sh
python mvc_pattern.py
```

You should see a window with an entry field, and when you enter a valid email address and click save, it will be saved to a file. Invalid email addresses will show an error message.

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
