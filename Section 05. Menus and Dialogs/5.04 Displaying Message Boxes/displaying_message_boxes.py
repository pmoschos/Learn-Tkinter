import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Displaying Message Boxes Demo')

# Function to display an information message box
def show_info():
    messagebox.showinfo("Information", "This is an information message box.")

# Create a button to trigger the information message box
info_button = ttk.Button(root, text="Show Info", command=show_info)
info_button.pack(pady=10)

# Function to display a warning message box
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message box.")

# Create a button to trigger the warning message box
warning_button = ttk.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=10)

# Function to display an error message box
def show_error():
    messagebox.showerror("Error", "This is an error message box.")

# Create a button to trigger the error message box
error_button = ttk.Button(root, text="Show Error", command=show_error)
error_button.pack(pady=10)

# Run the application
root.mainloop()