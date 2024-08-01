# Progressbars with Threads ⏳

Learn how to connect a progress bar with a running thread in Tkinter. This guide covers how to create a progress bar that updates based on the progress of a background task running in a separate thread.

## Getting Started

First, make sure to import Tkinter, ttk, and threading.

### 1. 📦 **Importing Tkinter, ttk, and threading**

```python
import tkinter as tk
from tkinter import ttk
import threading
import time
```

### 2. ⏳ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x200')
root.title('Progressbar with Threads Demo')
```

### 3. ⏳ **Creating the Progress Bar**

Create a progress bar widget.

```python
progress = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
progress.pack(pady=20)
```

### 4. ⏳ **Defining the Long-Running Task**

Create a function that simulates a long-running task.

```python
def long_running_task():
    for i in range(100):
        time.sleep(0.1)  # Simulate a time-consuming task
        progress['value'] = i + 1
    progress['value'] = 100
```

### 5. ⏳ **Starting the Task in a Separate Thread**

Create a function to start the long-running task in a separate thread.

```python
def start_task():
    thread = threading.Thread(target=long_running_task)
    thread.start()
```

### 6. ⏳ **Creating the UI Elements**

Create a button to start the task.

```python
start_button = ttk.Button(root, text='Start Task', command=start_task)
start_button.pack(pady=10)
```

### 7. 📑 **Complete Code**

Here's the complete code demonstrating how to connect a progress bar with a running thread:

```python
import tkinter as tk
from tkinter import ttk
import threading
import time

# Create the main window
root = tk.Tk()
root.geometry('400x200')
root.title('Progressbar with Threads Demo')

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

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `progressbar_threads.py` and run it using the Python interpreter:

```sh
python progressbar_threads.py
```

You should see a window with a progress bar and a button that, when clicked, starts a long-running task in a separate thread and updates the progress bar.

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
