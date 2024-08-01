# Integrating Matplotlib 📊

Learn how to display a bar chart from Matplotlib in a Tkinter application. Integrating Matplotlib with Tkinter allows you to visualize data directly within your GUI application.

## Getting Started

First, make sure to import Tkinter and Matplotlib.

### 1. 📦 **Importing Tkinter and Matplotlib**

```python
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
```

### 2. 📊 **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('600x400')
root.title('Integrating Matplotlib Demo')
```

### 3. 📊 **Creating a Bar Chart with Matplotlib**

You can create a bar chart using Matplotlib.

```python
# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a bar chart
ax.bar(categories, values)

# Set the title and labels
ax.set_title('Sample Bar Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
```

### 4. 📊 **Embedding the Matplotlib Chart in Tkinter**

You can embed the Matplotlib chart in the Tkinter window using `FigureCanvasTkAgg`.

```python
# Create a canvas to display the chart
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)
```

### 5. 📑 **Complete Code**

Here's the complete code demonstrating how to integrate Matplotlib in a Tkinter application:

```python
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main window
root = tk.Tk()
root.geometry('600x400')
root.title('Integrating Matplotlib Demo')

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a bar chart
ax.bar(categories, values)

# Set the title and labels
ax.set_title('Sample Bar Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# Create a canvas to display the chart
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `integrating_matplotlib.py` and run it using the Python interpreter:

```sh
python integrating_matplotlib.py
```

You should see a window displaying a bar chart created with Matplotlib.

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
