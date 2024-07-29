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