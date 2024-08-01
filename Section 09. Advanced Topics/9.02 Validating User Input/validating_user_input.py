import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Validating User Input Demo')

# Define the validation function
def validate_number(action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if action != '1':  # If the action is not insertion, allow it
        return True
    if text in '0123456789':
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return False

# Register the validation function
vcmd = (root.register(validate_number), '%d', '%P', '%s', '%S', '%v', '%V', '%W')

# Create a label
label = ttk.Label(root, text="Enter a number:")
label.pack(pady=10)

# Create an entry widget with validation
entry = ttk.Entry(root, validate='key', validatecommand=vcmd)
entry.pack(pady=10)

# Create a button to get the entry value
def get_value():
    print("Entered value:", entry.get())

button = ttk.Button(root, text="Submit", command=get_value)
button.pack(pady=10)

# Run the application
root.mainloop()