import tkinter as tk
from tkinter import ttk
import threading
import time
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Full Project Implementation')

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

# Create a progress bar
progress = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
progress.pack(pady=20)

# Define a long-running task
def long_running_task():
    for i in range(100):
        time.sleep(0.1)  # Simulate a time-consuming task
        progress['value'] = i + 1
    progress['value'] = 100

# Start the task in a separate thread
def start_task():
    thread = threading.Thread(target=long_running_task)
    thread.start()

# Create a button to start the task
start_button = ttk.Button(root, text='Start Task', command=start_task)
start_button.pack(pady=10)

# Create an icon and menu for the system tray
def create_image():
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=(255, 0, 0))
    dc.rectangle((0, 0, width // 2, height // 2), fill=(0, 255, 0))
    dc.rectangle((0, height // 2, width // 2, height), fill=(0, 0, 255))
    dc.rectangle((width // 2, height // 2, width, height), fill=(255, 255, 0))
    return image

def on_quit(icon, item):
    icon.stop()
    root.quit()

icon = pystray.Icon("test_icon")
menu = (item('Quit', on_quit),)
icon.menu = pystray.Menu(*menu)
icon.icon = create_image()

def run_icon():
    icon.run()

icon_thread = threading.Thread(target=run_icon)
icon_thread.start()

# Run the application
root.mainloop()