import tkinter
from tkinter import messagebox, ttk
import csv

# stores the choices that the user inputs
user_choices = {}


# window setup
root = tkinter.Tk()
root.geometry("800x1000")
root.title("Car Questionnaire")

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
     return  # Return if any field is empty

# Made a Dictionary to repeat responses back to you almost as a way of saying are you sure?
 user_choices["Price"] = budget
 user_choices["Size"] = size
 user_choices["County"] = county
 user_choices["Exotic"] = exotic
 user_choices["Year"] = year
 user_choices["Gas"] = gas
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
             car_price = int(car[key][:-1])  # Remove the 'k' from the price and convert to integer
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
budget_label=tkinter.Label(root,text="1. Enter estimated car budget (in dollars):", fg='dark blue', font=("Times New Roman", 12))
budget_label.pack(anchor=tkinter.W)
choices=['10k-20k', '20k-40k', '40k-60k', '60k-85k', '85k-100k', '100k+']
budget_textbox=ttk.Combobox(root, values=choices)
budget_textbox.pack(anchor=tkinter.W)
budget_textbox.pack()

# body type
size_label=tkinter.Label(root,text="2. Enter your preferred car size:", fg='dark blue', font=("Times New Roman", 12))
size_label.pack(anchor=tkinter.W)
choices=['SUV', 'Minivan', 'Pick-up truck', 'Sedan', 'Roadster', 'Convertible', 'Wagon', 'Van', 'Any']
size_textbox=ttk.Combobox(root, values=choices)
size_textbox.pack(anchor=tkinter.W)

# county
county_label=tkinter.Label(root,text="3. Enter your county location:", fg='dark blue', font=("Times New Roman", 12))
county_label.pack(anchor=tkinter.W)
choices=['Morris' , 'Essex', 'Bergen', 'Passaic']
county_textbox=ttk.Combobox(root, values=choices)
county_textbox.pack(anchor=tkinter.W)


# exotic
exotic_label=tkinter.Label(root,text="4. Do you like exotic cars?:", fg='dark blue', font=("Times New Roman", 12))
exotic_label.pack(anchor=tkinter.W)
choices=['Yes', 'No']
exotic_textbox=ttk.Combobox(root, values=choices)
exotic_textbox.pack(anchor=tkinter.W)

# year
year_label=tkinter.Label(root,text="5. What year?:", fg='dark blue', font=("Times New Roman", 12))
year_label.pack(anchor=tkinter.W)
choices=['2019','2020','2021','2022', '2023', '2024',]
year_textbox=ttk.Combobox(root, values=choices)
year_textbox.pack(anchor=tkinter.W)

# gas type
gas_label=tkinter.Label(root,text="6. Gas, Hybrid or Ev?:", fg='dark blue', font=("Times New Roman", 12))
gas_label.pack(anchor=tkinter.W)
choices=['Hybrid', 'Electric', 'Gas']
gas_textbox=ttk.Combobox(root, values=choices)
gas_textbox.pack(anchor=tkinter.W)

# make
brand_label=tkinter.Label(root,text="7. What Car brands do you prefer from the list (only choose one), answer other if it's none of the above?:", fg='dark blue', font=("Times New Roman", 12))
brand_label.pack(anchor=tkinter.W)
choices=['Porsche', 'Volvo', 'Ford', 'Toyota', 'Lamborghini','Tesla','Honda', 'Chevrolet', 'Nissan', 'Mazda','Other']
brand_textbox=ttk.Combobox(root, values=choices)
brand_textbox.pack(anchor=tkinter.W)


def open_second_page(user_choices, filtered_data):
   second_page = tkinter.Tk()
   second_page.geometry("800x1000")
   second_page.title("Car")
   label = tkinter.Label(second_page, text="Next")
   label.pack()

   # this shows what the user inputs and prints it to the second page
   for key, value in user_choices.items():
       label_text = key + ": " + value
       label = tkinter.Label(second_page, text=label_text)
       label.pack()

   # Display the data in a text widget
   text_widget = tkinter.Text(second_page, height=20, width=80, state='disabled')
   text_widget.pack()

   # Set the state to normal to allow inserting text
   text_widget.config(state="normal")

   # Add a heading
   text_widget.insert(tkinter.END, "Filtered Data:\n\n")

   # Iterate over the filtered data and display each car's information
   for car in filtered_data:
       text_widget.insert(tkinter.END, "Brand: {}\n".format(car['Brand']))
       text_widget.insert(tkinter.END, "Price: {}\n".format(car['Price']))
       text_widget.insert(tkinter.END, "Model: {}\n".format(car['Model']))
       text_widget.insert(tkinter.END, "Year: {}\n".format(car['Year']))
       text_widget.insert(tkinter.END, "Size: {}\n".format(car['Size']))
       text_widget.insert(tkinter.END, "County: {}\n".format(car['County']))
       text_widget.insert(tkinter.END, "Exotic: {}\n".format(car['Exotic']))
       text_widget.insert(tkinter.END, "Gas: {}\n".format(car['Gas']))
       text_widget.insert(tkinter.END, "Link: {}\n".format(car['Link']))
       text_widget.insert(tkinter.END, "\n")

   # Set the state back to disabled to make it read-only
   text_widget.config(state="disabled")

   second_page.mainloop()



with open('Car.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)


# submit
submit_button=tkinter.Button(root,text='Submit',command=OnClick_Submit , fg='red', font=("Times New Roman", 12))
submit_button.pack()
root.mainloop()
