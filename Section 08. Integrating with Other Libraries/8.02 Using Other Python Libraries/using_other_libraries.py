import tkinter as tk
from tkinter import ttk
import requests

# Create the main window
root = tk.Tk()
root.geometry('400x300')
root.title('Using Other Python Libraries Demo')

# Function to fetch data from an API
def fetch_data():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    if response.status_code == 200:
        data = response.json()
        display_data(data)
    else:
        print("Failed to fetch data")

# Function to display data in Tkinter
def display_data(data):
    rates = data.get('rates', {})
    for currency, rate in rates.items():
        label = ttk.Label(root, text=f"{currency}: {rate}")
        label.pack(pady=2)

# Create a button to fetch data
fetch_button = ttk.Button(root, text="Fetch Exchange Rates", command=fetch_data)
fetch_button.pack(pady=20)

# Run the application
root.mainloop()