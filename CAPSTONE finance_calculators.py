import math

# The import math module is required.

# The below is pseudocode.

'''Start:
Create a new file and call it finance calculators.
Save it as python in a VS Code folder.
Enter import math to the start of the file.
Create a variable and use print function to output block print.
Use input to ask user to choose between investment and bond.
Output using the print function.
Use if..else statement. 
For investment:
Ask user to enter amount, interest rate and time in years.
Output using print function. 
Use if...else statement.
Ask user to input if they want simple or compound interest.
Nest if.. elif statement.
This will confirm that user wants simple or compound interest.
Nest if..else statement for simple/compound calculations.
Use elif statement to state that bond has been input.
This will output message to user.
Ask user to input amount, interest rate and time in months.
Output using print function.
Calculate repayments per month using formula.
Output using print function.
Use else to print error message.
End'''


options = (
 """
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount that you would need to pay on a home loan 
""")

print(options)

user_entry = input("Please choose between investment and bond: ")

print(user_entry)


if user_entry == "investment":
    print("Please enter the following information, amount, interest rate and time in years.")

    user_amount = int(input("Please enter the amount: "))

    print('Amount Entered:',user_amount)

    interest_rate = int(input("Please enter the interest rate: "))

    print('Interest Rate Entered:',interest_rate)

    user_time = int(input("Please enter the time in years: "))

    print('Time Entered:',user_time)

    interest = input("Please state if you want compound or simple interest: ")

    print(interest)


    if interest == "simple":
     print("You have chosen simple interest.")

     interest = 0

     interest = user_amount *(1 + interest_rate * user_time)/100
     print(interest)

    elif interest == "compound":
     print("You have chosen compound interest")
     interest = 0

     interest = user_amount * math.pow((1 + interest_rate),user_time)/100
     print(interest)
    

elif user_entry == "bond":
    print("Please enter the amount, interest rate and time in months.")

    user_amount = int(input("Please enter the amount: "))
    print('Amount Entered:',user_amount)

    interest_rate = int(input("Please enter the interest rate: "))

    print('Interest Rate Entered:',interest_rate)

    user_time = float(input("Please enter the time in months: "))
    
    print('Time Entered:',user_time)

    repayment_amount = 0

    repayment_amount = (interest_rate * user_amount)/(1-(1 + interest_rate) ** (-user_time))/100

    print(repayment_amount)

else:
    print("Error: Please choose either investment or bond")

# The if, elif, else statement shows the end result.
    
# I have ended with the else statement, asking the user the relevant question again.
    
# The totals are showing the formulaic response for each.
    
# The totals are used to tell the user how much each will be.


    



    

     
    

















    






   
  





