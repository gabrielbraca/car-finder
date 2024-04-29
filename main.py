from tkinter import messagebox, ttk
import csv
from PIL import ImageTk,Image
import tkinter

# Function to extract digits manually from a given string
def extract_digits(value):
    numeric = ''
    # Loop through each character in the string
    for char in value:
        # it will append numbers that are between 0 and 9 and turn it to numeric string
        if '0' <= char <= '9':
            numeric += char
    # Turns collected digits into an integer
    return int(numeric)

def start_page():
    start = tkinter.Tk()
    start.geometry("1000x1000")
    start.title("Welcome to Car Questionnaire")

    # Added this line to set the background color
    start.configure(bg='#181818')

    Ford_img = ImageTk.PhotoImage(Image.open("Ford.jpeg"))

    # Create a Label widget to display the image
    Ford_label = tkinter.Label(start, image=Ford_img, bg='#1E1E1E')
    Ford_label.place(x=20, y=200)

    Chevorlette_img = ImageTk.PhotoImage(Image.open("Chevorlette.jpg"))

    # Create a Label widget to display the image
    Chevorlette_label = tkinter.Label(start, image=Chevorlette_img, bg='#1E1E1E')
    Chevorlette_label.place(x=350, y=200)

    Honda_img = ImageTk.PhotoImage(Image.open("Honda.jpg"))

    # Create a Label widget to display the image
    Honda_label = tkinter.Label(start, image=Honda_img, bg='#1E1E1E')
    Honda_label.place(x=680, y=200)

    Lambo_img = ImageTk.PhotoImage(Image.open("Lambo.jpeg"))

    # Create a Label widget to display the image
    Lambo_label = tkinter.Label(start, image=Lambo_img, bg='#1E1E1E')
    Lambo_label.place(x=20, y=400)

    Mazda_img = ImageTk.PhotoImage(Image.open("Mazda.jpeg"))

    # Create a Label widget to display the image
    Mazda_label = tkinter.Label(start, image=Mazda_img, bg='#1E1E1E')
    Mazda_label.place(x=350, y=400)

    Nissan_img = ImageTk.PhotoImage(Image.open("Nissan.jpeg"))

    # Create a Label widget to display the image
    Nissan_label = tkinter.Label(start, image=Nissan_img, bg='#1E1E1E')
    Nissan_label.place(x=680, y=400)

    Porche_img = ImageTk.PhotoImage(Image.open("Porche.jpg"))

    # Create a Label widget to display the image
    Porche_label = tkinter.Label(start, image=Porche_img, bg='#1E1E1E')
    Porche_label.place(x=20, y=600)

    Tesla_img = ImageTk.PhotoImage(Image.open("Tesla.jpeg"))

    # Create a Label widget to display the image
    Tesla_label = tkinter.Label(start, image=Tesla_img, bg='#1E1E1E')
    Tesla_label.place(x=350, y=600)


    Toyota_img = ImageTk.PhotoImage(Image.open("Toyota.jpg"))

    # Create a Label widget to display the image
    Toyota_label = tkinter.Label(start, image=Toyota_img, bg='#1E1E1E')
    Toyota_label.place(x=680, y=600)


    # Function to open the main page and close the start page
    def open_main_page():
        start.destroy()
        main_page()

    # Label and button for start page
    welcome_label = tkinter.Label(start, text="Welcome to Car Questionnaire!", fg="#CCCCCC", bg='#181818', font=("Comic Sans MS", 20))
    welcome_label.pack(pady=50)

    start_button = tkinter.Button(start, text="Start Questionnaire", command=open_main_page, fg='black', font=("Comic Sans MS", 18), bg='#CCCCCC')
    start_button.pack(pady=8)

    start.mainloop()

def main_page():
    # stores the choices that the user inputs
    user_choices = {}
    highlight_color = "#333333"

    # window setup
    root = tkinter.Tk()
    root.geometry("800x800")
    root.title("Car Questionnaire")

    # Adds a picture to top left
    img = tkinter.PhotoImage(file=r"car.png")
    root.iconphoto(False, img)

    # Added this line to set the background color
    root.configure(bg='#181818')

    # Loads the data from CSV
    def load_data(csv_file):
        data = []
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data

    # Loads data from CSV
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

        # Made a dictionary to repeat responses back to you
        user_choices["Price"] = budget
        user_choices["Size"] = size
        user_choices["County"] = county
        user_choices["Exotic"] = exotic
        user_choices["Year"] = year
        user_choices["Fuel"] = gas
        user_choices["Brand"] = brand
        print("User Choices:", user_choices)

        filtered_data = []

        # Loop through each car and apply the filtering logic
        for car in car_data:
            match = True

            # Loop through user choices to check if the car matches the user's selections
            for key, value in user_choices.items():
                if key == "Price" and value:
                    # Price range logic: convert 'k' to thousands and check if within range
                    price_range = [int(p[:-1]) for p in value.split('-')]
                    min_price, max_price = price_range[0], price_range[1]
                    car_price = int(car[key][:-1])
                    if not (min_price <= car_price <= max_price):
                        match = False
                        break
                elif car.get(key) != value:
                    # If any other key doesn't match, set match to False and break
                    match = False
                    break

            # If all user input matches a car that is in the csv it will print out
            if match:
                filtered_data.append(car)
        # Open the second page with unique filtered data
        print("Filtered Data:", filtered_data)

        # Display matching data on the second page
        open_second_page(user_choices, filtered_data)

    # Checks if all fields are filled
    if all(user_choices.values()):
        print('good')
    else:
        messagebox.showwarning("Warning", "Please Fill all the Fields")

    # asking user there budget
    budget_label = tkinter.Label(root, text="1. Enter estimated car budget (in dollars):", fg=fg_color,
                                 font=("Comic Sans MS", 17), bg='#181818', highlightbackground=highlight_color,
                                 highlightcolor=highlight_color)
    budget_label.pack(anchor=tkinter.W)
    choices = ['10k-20k', '20k-40k', '40k-60k', '60k-85k', '85k-600k']
    budget_textbox = ttk.Combobox(root, values=choices)
    budget_textbox.pack(anchor=tkinter.W)
    budget_textbox.pack()

    # asking user what body type
    size_label = tkinter.Label(root, text="2. Enter your preferred car body type:", fg=fg_color,
                               font=("Comic Sans MS", 17), bg='#181818', highlightbackground=highlight_color,
                               highlightcolor=highlight_color)
    size_label.pack(anchor=tkinter.W)
    choices = ['SUV', 'Mini-van', 'Pick-up Truck', 'Sedan', 'Convertible', 'Van']
    size_textbox = ttk.Combobox(root, values=choices)
    size_textbox.pack(anchor=tkinter.W)

    # asking user what county
    county_label = tkinter.Label(root, text="3. Enter your county location:", fg=fg_color, font=("Comic Sans MS", 17),
                                 bg='#181818', highlightbackground=highlight_color, highlightcolor=highlight_color)
    county_label.pack(anchor=tkinter.W)
    choices = ['Morris', 'Essex', 'Bergen', 'Passaic']
    county_textbox = ttk.Combobox(root, values=choices)
    county_textbox.pack(anchor=tkinter.W)

    # asking user if exotic or not
    exotic_label = tkinter.Label(root, text="4. Do you like exotic cars?:", fg=fg_color, font=("Comic Sans MS", 17),
                                 bg='#181818', highlightbackground=highlight_color, highlightcolor=highlight_color)
    exotic_label.pack(anchor=tkinter.W)
    choices = ['Yes', 'No']
    exotic_textbox = ttk.Combobox(root, values=choices)
    exotic_textbox.pack(anchor=tkinter.W)

    # asking user for year
    year_label = tkinter.Label(root, text="5. What year?:", fg=fg_color, font=("Comic Sans MS", 17), bg='#181818',
                               highlightbackground=highlight_color, highlightcolor=highlight_color)
    year_label.pack(anchor=tkinter.W)
    choices = ['2019', '2020', '2021', '2022', '2023', '2024', ]
    year_textbox = ttk.Combobox(root, values=choices)
    year_textbox.pack(anchor=tkinter.W)

    # asking user for gas type
    gas_label = tkinter.Label(root, text="6. Gas, Hybrid, or Electric?:", fg=fg_color, font=("Comic Sans MS", 17),
                              bg='#181818', highlightbackground=highlight_color, highlightcolor=highlight_color)
    gas_label.pack(anchor=tkinter.W)
    choices = ['Hybrid', 'Electric', 'Gas']
    gas_textbox = ttk.Combobox(root, values=choices)
    gas_textbox.pack(anchor=tkinter.W)

    # asking user for make
    brand_label = tkinter.Label(root, text="7. What Car brand do you prefer from the list?:", fg=fg_color,
                                font=("Comic Sans MS", 17), bg='#181818', highlightbackground=highlight_color,
                                highlightcolor=highlight_color)
    brand_label.pack(anchor=tkinter.W)
    choices = ['Porsche', 'Volvo', 'Ford', 'Toyota', 'Lamborghini', 'Tesla', 'Honda', 'Chevrolet', 'Nissan', 'Mazda',
               'Any']
    brand_textbox = ttk.Combobox(root, values=choices)
    brand_textbox.pack(anchor=tkinter.W)

    # Adds a Ford Picture
    my_img = ImageTk.PhotoImage(Image.open("imporannt.jpg"))
    my_label = tkinter.Label(image=my_img)
    my_label.place(x=500, y=520)

    # Adds a Lamborghini Huracán Photo
    my_img2 = ImageTk.PhotoImage(Image.open("lamborghini-1819204_640.jpg"))
    my_label2 = tkinter.Label(image=my_img2)
    my_label2.place(x=360, y=525)

    my_img3 = ImageTk.PhotoImage(Image.open("camaro-4331510_640.jpg"))
    my_label3 = tkinter.Label(image=my_img3)
    my_label3.place(x=200, y=520)

    # making a second page
    def open_second_page(user_choices, filtered_data):
        second_page = tkinter.Tk()
        second_page.geometry("800x1000")
        second_page.title("Car Answers")
        second_page.configure(bg='#1E1E1E')
        # Set the background color of the second page
        label = tkinter.Label(second_page, bg='#181818', fg=fg_color)
        label.pack()

        # Show user choices
        for key, value in user_choices.items():
            label_text = key + ": " + value
            label = tkinter.Label(second_page, text=label_text, bg='#181818', fg=fg_color)
            label.pack()

        # Display the data in a text widget
        text_widget = tkinter.Text(second_page, height=20, width=80, state='normal')
        text_widget.pack()

        # Set the state too normal to allow inserting text
        text_widget.config(state="normal")

        # Add a heading for exact matches
        text_widget.insert(tkinter.END, "Exact Matches:\n\n")

        # Display exact matches
        filtered_data = get_recommended_cars(user_choices, filtered_data)
        for car in filtered_data:
            display_car_info_text_widget(text_widget, car)

        # Show recommended cars
        text_widget.insert(tkinter.END, "\nRecommended Cars:\n\n")
        recommended_cars = get_recommended_cars(user_choices, car_data)
        for car in recommended_cars:
            display_car_info_text_widget(text_widget, car)

        # Set the state back to disabled to make it read only
        text_widget.config(state="disabled")

        # Quit button for second page
        quit_button = tkinter.Button(second_page, text='Quit', command=second_page.destroy, fg='red', font=("Comic Sans MS", 15), bg='black')
        quit_button.pack()

        # making a back button
        back_button = tkinter.Button(second_page, text='Back', command=second_page.destroy, fg='red',
                                     font=("Comic Sans MS", 15), bg='black')
        back_button.place(x=10, y=10)

        second_page.mainloop()

    def display_car_info_text_widget(text_widget, car):
        text_widget.insert(tkinter.END, "Brand: {}\n".format(car['Brand']))
        text_widget.insert(tkinter.END, "Price: {}\n".format(car['Price']))
        text_widget.insert(tkinter.END, "Model: {}\n".format(car['Model']))
        text_widget.insert(tkinter.END, "Year: {}\n".format(car['Year']))
        text_widget.insert(tkinter.END, "Size: {}\n".format(car['Size']))
        text_widget.insert(tkinter.END, "County: {}\n".format(car['County']))
        text_widget.insert(tkinter.END, "Exotic: {}\n".format(car['Exotic']))
        text_widget.insert(tkinter.END, "Fuel: {}\n".format(car['Fuel']))
        text_widget.insert(tkinter.END, "Link: {}\n".format(car['Link']))
        text_widget.insert(tkinter.END, "\n")

    def get_recommended_cars(user_choices, car_data):
        recommended_cars = []
        # Loop through the car data
        for car in car_data:
            # Extract numeric value from the price
            car_price = extract_digits(car["Price"])

            # Get the min and max price from user choices
            price_range = user_choices["Price"].split('-')
            min_price = extract_digits(price_range[0])
            max_price = extract_digits(price_range[1])

            # Check if the car matches the user's criteria
            if (min_price <= car_price <= max_price and
                    car["Fuel"] == user_choices["Fuel"] and
                    car["Size"] == user_choices["Size"]):
                recommended_cars.append(car)

        # Debugging print statement
        print("Recommended Cars:", recommended_cars)
        return recommended_cars

    # making a third page
    def open_third_page():
        third_page = tkinter.Toplevel()
        third_page.geometry("1000x1000")
        third_page.title("Body Types")
        third_page.configure(bg='#1E1E1E')
        # Set the background color of the second page

        # back button for third page
        back2_button = tkinter.Button(third_page, text='Back', command=third_page.destroy, fg='red',
                                      font=("Comic Sans MS", 15), bg='black')
        back2_button.place(x=10,y=10)

        # Load the sedan image
        sedan_img = ImageTk.PhotoImage(Image.open("Sedan.png"))

        # Create a Label widget to display the image
        sedan_label = tkinter.Label(third_page, image=sedan_img, bg='#1E1E1E')
        sedan_label.place(x=200, y=65)

        # Ensure the image is retained by storing a reference
        sedan_label.image = sedan_img

        # Load the suv image
        suv_img = ImageTk.PhotoImage(Image.open("SUV.png"))

        # Create a Label widget to display the image
        suv_label = tkinter.Label(third_page, image=suv_img, bg='#1E1E1E')
        suv_label.place(x=550, y=50)

        # Ensure the image is retained by storing a reference
        suv_label.image = suv_img

        # Load the convertible image
        Convertible_img = ImageTk.PhotoImage(Image.open("Convertible.png"))

        # Create a Label widget to display the image
        Convertible_label = tkinter.Label(third_page, image=Convertible_img, bg='#1E1E1E')
        Convertible_label.place(x=200, y=330)

        # Ensure the image is retained by storing a reference
        Convertible_label.image = Convertible_img

        minivan_img = ImageTk.PhotoImage(Image.open("minivan.png"))

        # Create a Label widget to display the image
        minivan_label = tkinter.Label(third_page, image=minivan_img, bg='#1E1E1E')
        minivan_label.place(x=550, y=300)

        # Ensure the image is retained by storing a reference
        minivan_label.image = minivan_img

        Pickup_img = ImageTk.PhotoImage(Image.open("Pickup.png"))

        # Create a Label widget to display the image
        Pickup_label = tkinter.Label(third_page, image=Pickup_img, bg='#1E1E1E')
        Pickup_label.place(x=350, y=600)

        # Ensure the image is retained by storing a reference
        Pickup_label.image = Pickup_img

    with open('Car.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

    # submit for first page
    submit_button = tkinter.Button(root, text='Submit', command=OnClick_Submit, fg='red', font=("Comic Sans MS", 18),
                                   bg='black')
    submit_button.pack()

    # Function to reset all the textboxes
    def reset_textboxes():
        budget_textbox.set('')
        size_textbox.set('')
        county_textbox.set('')
        exotic_textbox.set('')
        year_textbox.set('')
        gas_textbox.set('')
        brand_textbox.set('')

    # Reset button for questioning pages
    reset_button = tkinter.Button(root, text='Reset', command=reset_textboxes, fg='red',
                                  font=("Comic Sans MS", 18), bg='black')
    reset_button.place(x=0, y=415)

    # Button to open second page showing body types
    body_types_button = tkinter.Button(root, text="Don't know what body types are? Click here to find out ",
                                       command=open_third_page, fg='Purple', font=("Comic Sans MS", 18), bg='black')
    body_types_button.place(x=160, y=600)


    # quit button for first page
    quit_button = tkinter.Button(root, text='Quit', command=root.destroy, fg='red', font=("Comic Sans MS", 18), bg='black')
    quit_button.pack()
    root.mainloop()
start_page()