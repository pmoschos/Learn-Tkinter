import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Geometry Management Demo')

# Using pack
label1 = tk.Label(root, text="Pack - Top", bg="lightblue")
label1.pack(side="top", fill="x")

label2 = tk.Label(root, text="Pack - Bottom", bg="lightgreen")
label2.pack(side="bottom", fill="x")

label3 = tk.Label(root, text="Pack - Left", bg="lightyellow")
label3.pack(side="left", fill="y")

label4 = tk.Label(root, text="Pack - Right", bg="lightpink")
label4.pack(side="right", fill="y")

# Using grid
frame = tk.Frame(root, bg="lightgray")
frame.pack(pady=10)

label5 = tk.Label(frame, text="Grid - 0,0", bg="lightblue")
label5.grid(row=0, column=0, padx=5, pady=5)

label6 = tk.Label(frame, text="Grid - 0,1", bg="lightgreen")
label6.grid(row=0, column=1, padx=5, pady=5)

label7 = tk.Label(frame, text="Grid - 1,0", bg="lightyellow")
label7.grid(row=1, column=0, padx=5, pady=5)

label8 = tk.Label(frame, text="Grid - 1,1", bg="lightpink")
label8.grid(row=1, column=1, padx=5, pady=5)

# Using place
label9 = tk.Label(root, text="Place - (50, 50)", bg="lightblue")
label9.place(x=50, y=50)

label10 = tk.Label(root, text="Place - (150, 100)", bg="lightgreen")
label10.place(x=150, y=100)

label11 = tk.Label(root, text="Place - (250, 150)", bg="lightyellow")
label11.place(x=250, y=150)

# Run the application
root.mainloop()