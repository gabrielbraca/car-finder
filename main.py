import tkinter
from tkinter import messagebox, ttk
import csv

root = tkinter.Tk()
root.geometry("800x1000")

# stores the choices that the user inputs
user_choices = {}
def OnClick_Submit():
 budget=budget_textbox.get()
 size=size_textbox.get()
 county=county_textbox.get()
 miles=miles_textbox.get()
 lease_own=lease_own_textbox.get()
 exotic=exotic_textbox.get()
 year=year_textbox.get()
 gas=gas_textbox.get()
 brand=brand_textbox.get()

 user_choices["budget"] = budget
 user_choices["size"] = size
 user_choices["county"] = county
 user_choices["miles"] = miles
 user_choices["lease_own"] = lease_own
 user_choices["exotic"] = exotic
 user_choices["year"] = year
 user_choices["gas"] = gas
 user_choices["brand"] = brand

# checks if all the drop down menus are filled
 if all(user_choices.values()):
     messagebox.showinfo("Status", "Data Submitted")
     open_second_page(user_choices)
 else:
     messagebox.showwarning("Warning","Please Fill all the Fields")
root.title("Car Questionnaire")
budget_label=tkinter.Label(root,text="1. Enter estimated car budget (in dollars):", fg='dark blue', font=("Times New Roman", 12))
budget_label.pack(anchor=tkinter.W)
choices=['1k-10k' , '10k-20k', '20k-40k', '50k-70k', '70k-80k', '85k-100k', '100k+']
budget_textbox=ttk.Combobox(root, values=choices)
budget_textbox.pack(anchor=tkinter.W)
budget_textbox.pack()

size_label=tkinter.Label(root,text="2. Enter your preferred car size:", fg='dark blue', font=("Times New Roman", 12))
size_label.pack(anchor=tkinter.W)
choices=['SUV', 'Minivan', 'pickup', 'sedan', 'off-road' 'luxury', 'sport', 'truck', 'van', 'any']
size_textbox=ttk.Combobox(root, values=choices)
size_textbox.pack(anchor=tkinter.W)

county_label=tkinter.Label(root,text="3. Enter your county location:", fg='dark blue', font=("Times New Roman", 12))
county_label.pack(anchor=tkinter.W)
choices=['Morris' , 'Essex', 'Bergen']
county_textbox=ttk.Combobox(root, values=choices)
county_textbox.pack(anchor=tkinter.W)


exotic_label=tkinter.Label(root,text="8. Do you liked exotic cars?:", fg='dark blue', font=("Times New Roman", 12))
exotic_label.pack(anchor=tkinter.W)
choices=['yes', 'no']
exotic_textbox=ttk.Combobox(root, values=choices)
exotic_textbox.pack(anchor=tkinter.W)

year_label=tkinter.Label(root,text="9. What year?:", fg='dark blue', font=("Times New Roman", 12))
year_label.pack(anchor=tkinter.W)
choices=['2019','2020','2021','2022', '2023', '2024',]
year_textbox=ttk.Combobox(root, values=choices)
year_textbox.pack(anchor=tkinter.W)

gas_label=tkinter.Label(root,text="10. Gas, Hybrid or Ev?:", fg='dark blue', font=("Times New Roman", 12))
gas_label.pack(anchor=tkinter.W)
choices=['Hybrid', 'Electrical', 'Gas']
gas_textbox=ttk.Combobox(root, values=choices)
gas_textbox.pack(anchor=tkinter.W)

brand_label=tkinter.Label(root,text="11. What Car brands do you prefer from the list (only choose one), answer other if it's none of the above?:", fg='dark blue', font=("Times New Roman", 12))
brand_label.pack(anchor=tkinter.W)
choices=['Porsche', 'Volvo', 'Ford', 'Toyota', 'Lamborghini','Tesla','Honda', 'Chevrolet', 'Nissan', 'Mazda','Other']
brand_textbox=ttk.Combobox(root, values=choices)
brand_textbox.pack(anchor=tkinter.W)
def open_second_page(user_choices):
   second_page = tkinter.Tk()
   second_page.geometry("800x1000")
   second_page.title("Car")

   # this shows what the user inputs and prints it to the second page
   for key, value in user_choices.items():
       label_text = key + ": " + value
       label = tkinter.Label(second_page, text=label_text)
       label.pack()

    # reads the file
   with open('src/Gooder file for python - Sheet1.csv', 'r') as csv_file:
       csv_reader = csv.DictReader(csv_file)

       for line in csv_reader:
           print(line)
submit_button=tkinter.Button(root,text='Submit',command=OnClick_Submit , fg='red', font=("Times New Roman", 12))
submit_button.pack()
root.mainloop()

print(user_choices["brand"])
