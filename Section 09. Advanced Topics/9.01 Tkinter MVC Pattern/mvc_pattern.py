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