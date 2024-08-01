# Using Other Python Libraries 🔗

Explore how to integrate Tkinter with other Python libraries to enhance functionality. By leveraging various libraries, you can create more powerful and feature-rich applications.

## Getting Started

First, make sure to import Tkinter and any other Python libraries you need. In this example, we'll integrate Tkinter with the `requests` library to fetch data from an API and display it in the Tkinter application.

### 1. 📦 **Importing Tkinter and Other Libraries**

```python
import tkinter as tk
from tkinter import ttk
import requests
```

### 2. 🔗 **Creating the Main Window**

Initialize the Tkinter main window.

```python
root = tk.Tk()
root.geometry('400x300')
root.title('Using Other Python Libraries Demo')
```

### 3. 🔗 **Fetching Data from an API**

Use the `requests` library to fetch data from an API.

```python
def fetch_data():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    if response.status_code == 200:
        data = response.json()
        display_data(data)
    else:
        print("Failed to fetch data")
```

### 4. 🔗 **Displaying Data in Tkinter**

Display the fetched data in the Tkinter window.

```python
def display_data(data):
    rates = data.get('rates', {})
    for currency, rate in rates.items():
        label = ttk.Label(root, text=f"{currency}: {rate}")
        label.pack(pady=2)
```

### 5. 🔗 **Creating a Button to Fetch Data**

Create a button to trigger the data fetch.

```python
# Create a button to fetch data
fetch_button = ttk.Button(root, text="Fetch Exchange Rates", command=fetch_data)
fetch_button.pack(pady=20)
```

### 6. 📑 **Complete Code**

Here's the complete code demonstrating how to integrate Tkinter with the `requests` library:

```python
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
```

## Running the Code

Save your code in a file named `using_other_libraries.py` and run it using the Python interpreter:

```sh
python using_other_libraries.py
```

You should see a window with a button that, when clicked, fetches and displays exchange rates from the API.

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
