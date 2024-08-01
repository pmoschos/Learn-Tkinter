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