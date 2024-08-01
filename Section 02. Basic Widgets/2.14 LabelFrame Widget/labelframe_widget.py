import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("LabelFrame Widget Example")

# Create and pack a LabelFrame widget
labelframe = ttk.LabelFrame(root, text="User Information", padding=(10, 10))
labelframe.pack(padx=10, pady=10, fill="both", expand=True)

# Add widgets to the LabelFrame
name_label = ttk.Label(labelframe, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

name_entry = ttk.Entry(labelframe)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

email_label = ttk.Label(labelframe, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

email_entry = ttk.Entry(labelframe)
email_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Configure grid weights for the LabelFrame
labelframe.columnconfigure(1, weight=1)

# Run the application
root.mainloop()