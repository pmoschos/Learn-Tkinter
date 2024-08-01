import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('600x400')
root.title('Advanced Layout Management Demo')

# Create a top frame and bottom frame
top_frame = ttk.Frame(root, height=200, relief="raised", padding=10)
top_frame.pack(side="top", fill="x")

bottom_frame = ttk.Frame(root, height=200, relief="sunken", padding=10)
bottom_frame.pack(side="bottom", fill="x")

# Add widgets to the top frame using grid
ttk.Label(top_frame, text="Top Left", background="lightblue").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
ttk.Label(top_frame, text="Top Center", background="lightgreen").grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
ttk.Label(top_frame, text="Top Right", background="lightyellow").grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Configure grid weights for top frame
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)

# Add widgets to the bottom frame using pack
ttk.Label(bottom_frame, text="Bottom Left", background="lightblue").pack(side="left", expand=True, fill="both", padx=5, pady=5)
ttk.Label(bottom_frame, text="Bottom Center", background="lightgreen").pack(side="left", expand=True, fill="both", padx=5, pady=5)
ttk.Label(bottom_frame, text="Bottom Right", background="lightyellow").pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Create a frame to hold placed widgets
place_frame = ttk.Frame(root, height=200, relief="groove", padding=10)
place_frame.pack(side="top", fill="x")

# Add widgets using place
ttk.Label(place_frame, text="Placed at (20, 20)", background="lightpink").place(x=20, y=20)
ttk.Label(place_frame, text="Placed at (100, 100)", background="lightcoral").place(x=100, y=100)
ttk.Label(place_frame, text="Placed at (200, 50)", background="lightgoldenrodyellow").place(x=200, y=50)

# Run the application
root.mainloop()