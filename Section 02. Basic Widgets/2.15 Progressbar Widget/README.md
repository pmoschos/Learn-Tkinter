# Progressbar Widget 📊

Learn how to use the progressbar widget to give feedback to the user about the progress of a long-running task in Tkinter. The Progressbar widget is a great way to indicate the status of a process.

## Getting Started

First, make sure to import Tkinter and ttk.

### 1. 📦 **Importing Tkinter and ttk**

```python
import tkinter as tk
from tkinter import ttk
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.title("Progressbar Widget Example")
root.geometry("300x100")
```

### 3. 📊 **Creating a Progressbar Widget**

You can create a Progressbar widget using the `Progressbar` class.

```python
# Create a Progressbar widget
progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progressbar.pack(pady=20)
```

### 4. 🔄 **Starting and Stopping the Progressbar**

You can control the progressbar using the `start` and `stop` methods.

```python
def start_progress():
    progressbar.start(10)  # Increment every 10ms

def stop_progress():
    progressbar.stop()

# Create Buttons to start and stop the progressbar
start_button = ttk.Button(root, text="Start", command=start_progress)
start_button.pack(side="left", padx=10)

stop_button = ttk.Button(root, text="Stop", command=stop_progress)
stop_button.pack(side="right", padx=10)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Progressbar widget:

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Progressbar Widget Example")
root.geometry("300x100")

# Create and pack a Progressbar widget
progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progressbar.pack(pady=20)

# Function to start the progressbar
def start_progress():
    progressbar.start(10)  # Increment every 10ms

# Function to stop the progressbar
def stop_progress():
    progressbar.stop()

# Create and pack Buttons to start and stop the progressbar
start_button = ttk.Button(root, text="Start", command=start_progress)
start_button.pack(side="left", padx=10)

stop_button = ttk.Button(root, text="Stop", command=stop_progress)
stop_button.pack(side="right", padx=10)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `progressbar_widget.py` and run it using the Python interpreter:

```sh
python progressbar_widget.py
```

You should see a window with a Progressbar widget and buttons to start and stop its progress.

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
