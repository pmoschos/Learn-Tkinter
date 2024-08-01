import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky='nsew')

# create frames
home_frame = ttk.Frame(notebook, width=400, height=280)
settings_frame = ttk.Frame(notebook, width=400, height=280)
profile_frame = ttk.Frame(notebook, width=400, height=280)
about_frame = ttk.Frame(notebook, width=400, height=280)

# add frames to notebook
notebook.add(home_frame, text='Home')
notebook.add(settings_frame, text='Settings')
notebook.add(profile_frame, text='Profile')
notebook.add(about_frame, text='About')

# add content to the tabs
ttk.Label(home_frame, text="Welcome to the Home tab").pack(pady=10, padx=10)
ttk.Label(settings_frame, text="Adjust your settings here").pack(pady=10, padx=10)
ttk.Label(profile_frame, text="User Profile Information").pack(pady=10, padx=10)
ttk.Label(about_frame, text="About this application").pack(pady=10, padx=10)

# Configure the grid to expand properly
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
