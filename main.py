import tkinter
from tkinter import messagebox, ttk
import csv


# stores the choices that the user inputs
user_choices = {}
highlight_color = "#333333"


# window setup
root = tkinter.Tk()
root.geometry("800x1000")
root.title("Car Questionnaire")
# Added this line to set the background color
root.configure(bg='#181818')
# Function to load data from CSV
def load_data(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


# Load data from CSV
car_data = load_data('Car.csv')
# Lighter shade of gray to highlight the letters
fg_color = "#CCCCCC"


def OnClick_Submit():
 budget = budget_textbox.get()
 size = size_textbox.get()
 county = county_textbox.get()
 exotic = exotic_textbox.get()
 year = year_textbox.get()
 gas = gas_textbox.get()
 brand = brand_textbox.get()

 # Check if any of the fields are empty
 if not all([budget, size, county, exotic, year, gas, brand]):
     # Show a warning message
     messagebox.showwarning("Warning", "Please fill out all the fields.")
     # Return if any field is empty
     return

# Made a Dictionary to repeat responses back to you almost as a way of saying are you sure?
 user_choices["Price"] = budget
 user_choices["Size"] = size
 user_choices["County"] = county
 user_choices["Exotic"] = exotic
 user_choices["Year"] = year
 user_choices["Fuel"] = gas
 user_choices["Brand"] = brand
 print("User Choices:", user_choices)


 # Filter data based on user choices
 filtered_data = []
 for car in car_data:
     match = True
     for key, value in user_choices.items():
         # Check if the key is "Price" and the car's price falls within the specified range
         if key == "Price" and value:
             price_range = value.split('-')
             # Remove the 'k' from the price and convert to integer
             car_price = int(car[key][:-1])
             min_price = int(price_range[0][:-1])
             max_price = int(price_range[1][:-1])
             if not (min_price <= car_price <= max_price):
                 match = False
                 break
         elif value and car.get(key, '') != value:
             match = False
             break
     if match:
         filtered_data.append(car)

 print("Filtered Data:", filtered_data)

 if filtered_data:
     # Display matching data on the second page
     open_second_page(user_choices, filtered_data)
 else:
     messagebox.showinfo("No Matches", "No cars match your criteria.")

 # Checks if all fields are filled
 if all(user_choices.values()):
     messagebox.showinfo("Status", "Data Submitted")
 else:
     messagebox.showwarning("Warning", "Please Fill all the Fields")

# budget
budget_label = tkinter.Label(root, text="1. Enter estimated car budget (in dollars):", fg=fg_color, font=("Comic Sans MS", 12), bg='#1E1E1E', highlightbackground=highlight_color, highlightcolor=highlight_color)
budget_label.pack(anchor=tkinter.W)
choices=['10k-20k', '20k-40k', '40k-60k', '60k-85k', '85k-100k', '100k-600k']
budget_textbox=ttk.Combobox(root, values=choices)
budget_textbox.pack(anchor=tkinter.W)
budget_textbox.pack()

# body type
size_label=tkinter.Label(root,text="2. Enter your preferred car size:",fg=fg_color, font=("Comic Sans MS", 12), bg='#1E1E1E', highlightbackground=highlight_color, highlightcolor=highlight_color)
size_label.pack(anchor=tkinter.W)
choices=['SUV', 'Mini-van', 'Pick-up truck', 'Sedan', 'Roadster', 'Convertible', 'Wagon', 'Van']
size_textbox=ttk.Combobox(root, values=choices)
size_textbox.pack(anchor=tkinter.W)

# county
county_label=tkinter.Label(root,text="3. Enter your county location:",fg=fg_color, font=("Comic Sans MS", 12), bg='#1E1E1E', highlightbackground=highlight_color, highlightcolor=highlight_color)
county_label.pack(anchor=tkinter.W)
choices=['Morris' , 'Essex', 'Bergen', 'Passaic']
county_textbox=ttk.Combobox(root, values=choices)
county_textbox.pack(anchor=tkinter.W)
