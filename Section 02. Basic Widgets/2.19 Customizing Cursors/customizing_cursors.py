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