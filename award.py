'''Start:
Create a file named award.
Save it in python in a folder in VS Code.
Create three variables for swimming, cycling, running.
Ask the user to input the time in minutes for each.
Use int to cast each input into a whole number.
Output each number by using the print function.
Create a new variable.
Then add the three numbers entered together to get a total. 
Use the print function to output total.
For the if,elif, else statement, state the minutes total.
Use if to check if user is less than or equal to the minutes total.
Use print function to state award received.
Use elif to check if the user is less than or equal to 105 minutes total.
Use print function to state award received.
Use elif to check if user is less than or equal to 110 minutes total.
Use print function to state award received.
Use else for more than 110 minutes after the 100 minutes total.
Use print function to output that no award is received.
End'''

swim_time = int(input("What was your swimming time in minutes?: "))
    
print(swim_time)

cycle_time = int(input("What was your cycling time in minutes?: "))
     
print(cycle_time)

run_time = int(input("What was your running time in minutes?: "))
     
print(run_time)

# I have used the input function to request the information

# I have used the print function to output the information

# The three input statements above cast the input for each into int(whole numbers)


mins_total = swim_time + cycle_time + run_time

print(mins_total)


# The mins_total is obtained by adding the three variables together using the plus sign and then printing

# I have left sufficient white space to enhance the code presentation

if  mins_total <=100:
      print("Provincial Colours")
elif mins_total <= 105: 
      print("Provincial Half Colours")
elif mins_total <=110:
      print("Provincial Scroll")
else:
      print("No award")


# The above if,elif,else statements print the award that is won or not for the race

# The else statement outputs that no award has been won




