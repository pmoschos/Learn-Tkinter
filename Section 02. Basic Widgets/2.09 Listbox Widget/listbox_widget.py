import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Listbox Widget Example")

# Create and pack a Listbox widget
listbox = tk.Listbox(root, height=10)
listbox.pack(padx=10, pady=10)

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Function to show the selected item
def show_selected_item():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected Item(s):", selected_items)

# Create and pack a Button to show the selected item
button = ttk.Button(root, text="Show Selected Item", command=show_selected_item)
button.pack(pady=10)

# Run the application
root.mainloop()