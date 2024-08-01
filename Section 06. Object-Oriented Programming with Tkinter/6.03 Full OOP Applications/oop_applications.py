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