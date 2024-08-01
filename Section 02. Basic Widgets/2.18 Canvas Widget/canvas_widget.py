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