import tkinter
from tkinter import messagebox, ttk
import csv


# stores the choices that the user inputs
user_choices = {}


# window setup
root = tkinter.Tk()
root.geometry("800x1000")
root.title("Car Questionnaire")

def OnClick_Submit():
 budget = budget_textbox.get()
 size = size_textbox.get()
 county = county_textbox.get()
 exotic = exotic_textbox.get()
 year = year_textbox.get()
 gas = gas_textbox.get()
 brand = brand_textbox.get()

 user_choices["Budget"] = budget
 user_choices["Size"] = size
 user_choices["County"] = county
 user_choices["Exotic"] = exotic
 user_choices["Year"] = year
 user_choices["Gas"] = gas
 user_choices["Brand"] = brand

 if all(user_choices.values()):
     messagebox.showinfo("Status", "Data Submitted")
     open_second_page(user_choices)
 else:
     messagebox.showwarning("Warning","Please Fill all the Fields")

# budget
budget_label=tkinter.Label(root,text="1. Enter estimated car budget (in dollars):", fg='dark blue', font=("Times New Roman", 12))
budget_label.pack(anchor=tkinter.W)
choices=['10k-20k', '20k-40k', '50k-70k', '70k-80k', '85k-100k', '100k+']
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
exotic_label=tkinter.Label(root,text="4. Do you liked exotic cars?:", fg='dark blue', font=("Times New Roman", 12))
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
choices=['Hybrid', 'Electrical', 'Gas']
gas_textbox=ttk.Combobox(root, values=choices)
gas_textbox.pack(anchor=tkinter.W)

# make
brand_label=tkinter.Label(root,text="7. What Car brands do you prefer from the list (only choose one), answer other if it's none of the above?:", fg='dark blue', font=("Times New Roman", 12))
brand_label.pack(anchor=tkinter.W)
choices=['Porsche', 'Volvo', 'Ford', 'Toyota', 'Lamborghini','Tesla','Honda', 'Chevrolet', 'Nissan', 'Mazda','Other']
brand_textbox=ttk.Combobox(root, values=choices)
brand_textbox.pack(anchor=tkinter.W)


def open_second_page(user_choices):
   second_page = tkinter.Tk()
   second_page.geometry("800x1000")
   second_page.title("Car")
   label = tkinter.Label(root, text="Next")
   label.pack()

   # this shows what the user inputs and prints it to the second page
   for key, value in user_choices.items():
       label_text = key + ": " + value
       label = tkinter.Label(second_page, text=label_text)
       label.pack()


with open('Car.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)


# submit
submit_button=tkinter.Button(root,text='Submit',command=OnClick_Submit , fg='red', font=("Times New Roman", 12))
submit_button.pack()
root.mainloop()
