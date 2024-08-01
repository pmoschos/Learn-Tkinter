import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('300x250')
root.title('Temperature Converter')

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

# Fahrenheit label and entry
fahrenheit_label = ttk.Label(root, text="Fahrenheit:")
fahrenheit_label.pack(pady=5)

fahrenheit_var = tk.StringVar()
fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_var)
fahrenheit_entry.pack(pady=5)

# Celsius label
celsius_label = ttk.Label(root, text="Celsius:")
celsius_label.pack(pady=5)

celsius_var = tk.StringVar()
celsius_entry = ttk.Entry(root, textvariable=celsius_var, state='readonly')
celsius_entry.pack(pady=5)

# Function to convert temperature and update the Celsius entry
def convert_temperature():
    try:
        fahrenheit = float(fahrenheit_var.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        celsius_var.set(f"{celsius:.2f}")
    except ValueError:
        celsius_var.set("Invalid input")

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

# Run the application
root.mainloop()