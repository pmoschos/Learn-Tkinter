import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Using Dialogs Demo')

# Function to display a Yes/No dialog
def show_yes_no():
    result = messagebox.askyesno("Question", "Do you want to proceed?")
    print(f"Yes/No result: {result}")

# Create a button to trigger the Yes/No dialog
yes_no_button = ttk.Button(root, text="Show Yes/No", command=show_yes_no)
yes_no_button.pack(pady=10)

# Function to display an OK/Cancel dialog
def show_ok_cancel():
    result = messagebox.askokcancel("Question", "Do you want to save changes?")
    print(f"OK/Cancel result: {result}")

# Create a button to trigger the OK/Cancel dialog
ok_cancel_button = ttk.Button(root, text="Show OK/Cancel", command=show_ok_cancel)
ok_cancel_button.pack(pady=10)

# Function to display a Retry/Cancel dialog
def show_retry_cancel():
    result = messagebox.askretrycancel("Question", "Do you want to retry the operation?")
    print(f"Retry/Cancel result: {result}")

# Create a button to trigger the Retry/Cancel dialog
retry_cancel_button = ttk.Button(root, text="Show Retry/Cancel", command=show_retry_cancel)
retry_cancel_button.pack(pady=10)

# Function to display an Open File dialog
def show_open_file():
    file_path = filedialog.askopenfilename(title="Open File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    print(f"Selected file: {file_path}")

# Create a button to trigger the Open File dialog
open_file_button = ttk.Button(root, text="Open File", command=show_open_file)
open_file_button.pack(pady=10)

# Run the application
root.mainloop()