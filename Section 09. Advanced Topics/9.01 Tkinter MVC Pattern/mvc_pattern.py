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