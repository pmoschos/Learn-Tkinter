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