'''Start
Create a file named cafe.
Save it as a python file in VS Code.
Create a variable called menu and store a list in it.
Create a price dictionary.
Store all the values for the keys stated in the list.
Create a stock dictionary.
Store all the values for the keys stated in the list.
Use a for loop to loop through the menu.
Use print function to output the total_amount.
End'''

# The below is the menu variable with a list of items

# Key value pairs will be shown in price_dict and stock_dict


menu = ["apples", "bananas", "oranges", "pears"]

price_dict = {
    "apples": 1.50,
    "bananas": 2,
    "oranges": 3,
    "pears": 2,
}

stock_dict = {
    "apples":7,
    "bananas":7,
    "oranges":8,
    "pears":9,
}

total_amount = 0  # I have initialised the variable

for item in menu:
    value = price_dict[item] * stock_dict[item] 
    total_amount += value
print(total_amount) 


# I have used a for loop to loop through the menu    

# I have used the print function to output total amount


















