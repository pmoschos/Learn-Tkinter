# System Tray Applications 🖥️

Learn how to develop a system tray application in Tkinter. This guide covers how to create a Tkinter application that runs in the system tray using the `pystray` library.

## Getting Started

First, make sure to install the `pystray` library. You can install it using pip:

```sh
pip install pystray
```

Also, you will need to install the `Pillow` library for handling icons:

```sh
pip install pillow
```

### 1. 📦 **Importing Required Libraries**

Import Tkinter, pystray, and other necessary modules.

```python
import tkinter as tk
from tkinter import ttk
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import threading
```

### 2. 🖥️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x200')
root.title('System Tray Application')
```

### 3. 🖥️ **Creating the System Tray Icon**

Create an icon and menu for the system tray.

```python
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
```

### 4. 🖥️ **Running the Icon in a Separate Thread**

Run the system tray icon in a separate thread.

```python
def run_icon():
    icon.run()

icon_thread = threading.Thread(target=run_icon)
icon_thread.start()
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to create a system tray application in Tkinter:

```python
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
```

## Running the Code

Save your code in a file named `system_tray_app.py` and run it using the Python interpreter:

```sh
python system_tray_app.py
```

You should see a window and an icon in the system tray. Clicking the "Quit" menu in the system tray icon will close the application.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧

Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
