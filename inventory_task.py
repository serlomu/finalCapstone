#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip3 install tabulate')
from tabulate import tabulate

# Main class
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# Methods
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        shoe_data = f'''Country: {self.country}Code: {self.code}Product: {self.product}Cost: {self.cost}Quantity: {self.quantity}'''
        return shoe_data

shoe_list = []

# function that will open the file and read the data
def read_shoes_data():

    inventory_file = "inventory.txt"
    inventory = []
    
    # block try except to test a block of code for errors
    try:
        with open(inventory_file, "r") as f:
            for count, item in enumerate(f):
                if count != 0:  
                    item = item.strip().split(",")
                    if len(item) == 5:  
                        inventory.append(item)
                    else:
                        raise Exception(f"The file is meant to have 5 rows, but has {len(item)} rows.")

 
    except FileNotFoundError as error:
        print("File inventory.txt not available")
        exit()

    # Stores the data in a list as a Shoe class
    for shoe in inventory:
        country = shoe[0]
        code = shoe[1]
        product = shoe[2]
        cost = float(shoe[3])
        quantity = int(shoe[4])

        shoe_list.append(Shoe(country, code, product, cost, quantity))

    return

# function for the user to itroduce a new entry/reference and append it
def capture_shoes():

    country = input("Enter the country: ")
    code = str(input("Enter the shoe code: "))
    product = input("Enter the product name: ")
    cost = int(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the quantity quantity of stock: "))

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    with open("inventory.txt", "a") as f:
        write_string = f"{country},{code},{product},{cost},{quantity}"
        f.write(write_string)

    return

# function that iterate to the list and print it

def view_all():

    header = ["Country", "Code", "Product", "Cost", "Quantity"]
    _shoe_list = [header]

    # Appending inventory data to the list
    for shoe in shoe_list:
        _shoe_list.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    # Prints the data 
    print(tabulate(_shoe_list) + "\n")
    return

# funtion that find the shoe with the lowest quantity

def re_stock():

    # Loops to find the shoe with the lowest quantity
    for count, shoe in enumerate(shoe_list):

        if count == 0:
            lowest_quantity = shoe


        if shoe.quantity < lowest_quantity.quantity:
            lowest_quantity = shoe

    print(f"The item with the lowest stock is:\n{lowest_quantity}")

    # Asks the user if they would like to restock the shoe, reprompts on an invalid answer
    while True:
        option = input("Would you like to add stock to this product? Y/N: ").lower()
        if option == "y" or option == "yes":
            while True:
                try:
                    extra_stock = int(input("How many shoes would you like to add: "))
                    lowest_quantity.quantity += extra_stock
                    break

                except:
                    print("Enter a valid number.\n")

            # Updates the quantity of the shoes
            count = 0
            for count, shoe in enumerate(shoe_list):
                if shoe.code == lowest_quantity.code:
                    shoe_list[count] = lowest_quantity

            # Writes the new inventory to the file
            with open("inventory.txt", "w") as f:
                header = "Country,Code,Product,Cost,Quantity\n"
                f.write(header)

                for shoe in shoe_list:
                    write_string = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                    f.write(write_string)

            print("Inventory updated successfully.\n")
            break
        elif option == "n" or option == "no":
            print()
            break
        else:
            print("Select a valid option.\n")

    return

# funtion that find a shoe introducing the code

def search_shoe():

    # Ask the user for the shoe code to search for
    shoe_code = input("Enter the shoe code: ").upper()

    # Loop through the inventory 
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            shoe_found = shoe
            return shoe_found
    search_fail = "Shoe not found.\n"

    return search_fail

#function calculate total value of all items

def value_per_item():

    header = ["Code", "Product", "Total Value (RMB)"]
    total_value_array = [header]

    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        total_value_array.append([shoe.code, shoe.product, total_value])

    print(tabulate(total_value_array) + "\n")

    return

# function that shows the product with the highest quantity

def highest_qty():

    for count, shoe in enumerate(shoe_list):
        # Initialise the higest quantity value with the first value in the list
        if count == 0:
            highest_quantity = shoe

        # Replaced previous high value if the logic finds a higher value
        if shoe.quantity > highest_quantity.quantity:
            highest_quantity = shoe

    print(f"The item with the highest stock is:\n{highest_quantity}\nYou should consider putting this on sale.\n")

    return


read_shoes_data()
print("INVENTORY")
print("---------")
while True:
    
    option = input("""Please select one of the following options:
v   - View all stock
a   - Add a new reference to the stock
h   - Displays the shoe with the highest stock
r   - Restock the shoe with the lowest stock
s   - Search for a shoe by the shoe code
vt  - Displays the total value for each item in the list
e   - Exit the inventory
Select:""")

    if option == "v":
        view_all()

    elif option == "a":
        capture_shoes()

    elif option == "h":
        highest_qty()

    elif option == "r":
        re_stock()

    elif option == "s":
        message = search_shoe()
        print(message)

    elif option == "vt":
        value_per_item()

    elif option == "e":
        print("Goodbye!")
        break

    else:
        print("Please choose a valid option.\n")
        


# In[ ]:




