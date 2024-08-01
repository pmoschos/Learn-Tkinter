# Canvas Widget 🎨

Learn how to use the Canvas widget in Tkinter. The Canvas widget allows you to create complex graphics, including shapes, lines, and images.

## Getting Started

First, make sure to import Tkinter.

### 1. 📦 **Importing Tkinter**

```python
import tkinter as tk
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('600x400')
root.title('Canvas Demo')
```

### 3. 🎨 **Creating a Canvas Widget**

You can create a Canvas widget using the `Canvas` class.

```python
# Create a Canvas widget
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(pady=20)
```

### 4. ➕ **Drawing Shapes on the Canvas**

You can draw various shapes on the Canvas, such as lines, rectangles, ovals, and polygons.

```python
# Draw a line
canvas.create_line(50, 50, 200, 50, fill='blue', width=2)

# Draw a rectangle
canvas.create_rectangle(50, 100, 200, 150, fill='red', outline='black', width=2)

# Draw an oval
canvas.create_oval(250, 50, 400, 150, fill='green', outline='black', width=2)

# Draw a polygon
canvas.create_polygon(450, 100, 500, 50, 550, 100, fill='purple', outline='black', width=2)
```

### 5. ➕ **Adding Text to the Canvas**

You can also add text to the Canvas using the `create_text` method.

```python
# Add text to the Canvas
canvas.create_text(300, 200, text='Hello, Canvas!', font=('Arial', 24), fill='black')
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating the usage of the Canvas widget:

```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry('600x400')
root.title('Canvas Demo')

# Create a Canvas widget
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(pady=20)

# Draw a line
canvas.create_line(50, 50, 200, 50, fill='blue', width=2)

# Draw a rectangle
canvas.create_rectangle(50, 100, 200, 150, fill='red', outline='black', width=2)

# Draw an oval
canvas.create_oval(250, 50, 400, 150, fill='green', outline='black', width=2)

# Draw a polygon
canvas.create_polygon(450, 100, 500, 50, 550, 100, fill='purple', outline='black', width=2)

# Add text to the Canvas
canvas.create_text(300, 200, text='Hello, Canvas!', font=('Arial', 24), fill='black')

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `canvas_widget.py` and run it using the Python interpreter:

```sh
python canvas_widget.py
```

You should see a window with a Canvas widget displaying various shapes and text.

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
