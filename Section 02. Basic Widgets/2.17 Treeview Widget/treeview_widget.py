import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('600x400')
root.title('Treeview Demo')

# Create a Treeview widget
tree = ttk.Treeview(root)
tree.pack(pady=20, fill='both', expand=True)

# Define columns
tree['columns'] = ('Name', 'Age', 'Email')

# Format columns
tree.column('#0', width=0, stretch=tk.NO)
tree.column('Name', anchor=tk.W, width=120)
tree.column('Age', anchor=tk.CENTER, width=80)
tree.column('Email', anchor=tk.W, width=200)

# Create headings
tree.heading('#0', text='', anchor=tk.W)
tree.heading('Name', text='Name', anchor=tk.W)
tree.heading('Age', text='Age', anchor=tk.CENTER)
tree.heading('Email', text='Email', anchor=tk.W)

# Add data
tree.insert(parent='', index='end', iid=0, text='', values=('John Doe', '30', 'john.doe@example.com'))
tree.insert(parent='', index='end', iid=1, text='', values=('Jane Smith', '25', 'jane.smith@example.com'))
tree.insert(parent='', index='end', iid=2, text='', values=('Mike Johnson', '40', 'mike.johnson@example.com'))

# Run the application
root.mainloop()