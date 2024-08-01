import tkinter as tk
from tkinter import ttk
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import threading

# Create the main window
root = tk.Tk()
root.geometry('400x200')
root.title('System Tray Application')

def create_image():
    # Generate an image
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=(255, 0, 0))
    dc.rectangle(
        (0, 0, width // 2, height // 2),
        fill=(0, 255, 0))
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=(0, 0, 255))
    dc.rectangle(
        (width // 2, height // 2, width, height),
        fill=(255, 255, 0))
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