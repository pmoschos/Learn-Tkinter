# Customizing Cursors 🖱️

Learn how to change the mouse cursor when it is over a widget in Tkinter. You can customize the cursor for various widgets to enhance the user experience.

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
root.geometry('400x300')
root.title('Customizing Cursors Demo')
```

### 3. 🖱️ **Changing the Cursor for a Widget**

You can change the cursor for a widget using the `cursor` option.

```python
# Create a button with a custom cursor
button = tk.Button(root, text='Hover over me', cursor='hand2')
button.pack(pady=20)

# Create a label with a custom cursor
label = tk.Label(root, text='Move the cursor here', cursor='cross')
label.pack(pady=20)

# Create an entry with a custom cursor
entry = tk.Entry(root, cursor='xterm')
entry.pack(pady=20)
```

### 4. 📑 **Complete Code**

Here's the complete code demonstrating how to customize cursors for various widgets:

```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Customizing Cursors Demo')

# Create a button with a custom cursor
button = tk.Button(root, text='Hover over me', cursor='hand2')
button.pack(pady=20)

# Create a label with a custom cursor
label = tk.Label(root, text='Move the cursor here', cursor='cross')
label.pack(pady=20)

# Create an entry with a custom cursor
entry = tk.Entry(root, cursor='xterm')
entry.pack(pady=20)

# Run the application
root.mainloop()
```

## Running the Code

Save your code in a file named `customizing_cursors.py` and run it using the Python interpreter:

```sh
python customizing_cursors.py
```

You should see a window with various widgets that change the cursor when you hover over them.

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
