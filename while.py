'''Start:
Create a file named while and save it as a python file in VS Code.
Write pseudocode to explain how to execute the task.
Use input function to ask user to enter a number.
Use print function to output the number.
Create a list all_numbers and a variable counter, initilise it.
Create a while loop that repeatedly asks the user to enter a number.
When the user enters -1, use break.
Calculate the average using sum and len functions.
Use print to output the average.
End'''

# The below variable all_numbers is a list

# The count variable has been initialised

all_numbers = []

count = 0

while True:
   entered_number = int(input("Please enter a whole number: "))
   if entered_number == -1:
      break
   all_numbers.append(entered_number)
   print(all_numbers)


# The input function is used to ask the user to enter a number.
   
# The above is a while loop using the variable entered_number.


num_average = sum(all_numbers) / len(all_numbers)
print(num_average)


# The above shows the average of the numbers entered.

# I have used the all_numbers variable as arguments for sum and len.







