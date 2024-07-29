
# Working with Tkinter Windows 🖼️

Learn how to manipulate various attributes of a Tkinter window including title, size, location, resizability, transparency, and stacking order.

## Getting Started

Tkinter provides a variety of options to customize your window. Let's explore these options step by step.

### 1. 📦 **Importing Tkinter**

As always, start by importing Tkinter.

```python
import tkinter as tk
```

### 2. 🖼️ **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
```

### 3. 📝 **Setting the Window Title**

You can set the title of the window using the `title` method.

```python
root.title("My Tkinter Window")
```

### 4. 📐 **Setting the Window Size**

Use the `geometry` method to set the size of the window. The format is `"widthxheight"`.

```python
root.geometry("800x600")
```

### 5. 📍 **Setting the Window Position**

You can also set the initial position of the window on the screen using the `geometry` method. The format is `"widthxheight+x+y"`.

```python
root.geometry("800x600+100+100")
```

### 6. 🔒 **Disabling Window Resizing**

If you want to disable resizing, use the `resizable` method with arguments `False`.

```python
root.resizable(False, False)
```

### 7. 🌫️ **Setting Window Transparency**

Set the transparency level of the window using the `attributes` method. The value ranges from `0.0` (completely transparent) to `1.0` (completely opaque).

```python
root.attributes("-alpha", 0.8)
```

### 8. 📚 **Setting the Stacking Order**

Control whether the window should always be on top of other windows using the `attributes` method.

```python
root.attributes("-topmost", True)
```

## Complete Code

Here's the complete code demonstrating the various window attributes:

```python
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("My Tkinter Window")

# Set the window size
root.geometry("800x600")

# Set the window size and position
root.geometry("800x600+100+100")

# Disable window resizing
root.resizable(False, False)

# Set window transparency
root.attributes("-alpha", 0.8)

# Always on top
root.attributes("-topmost", True)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `window_attributes.py` and run it using the Python interpreter:

```sh
python window_attributes.py
```

You should see a window with the specified attributes.

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
