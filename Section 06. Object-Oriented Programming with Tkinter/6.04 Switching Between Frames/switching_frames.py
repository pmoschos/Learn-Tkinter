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