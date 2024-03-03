'''Start:
Create a file named pattern and save it as python in VS Code.
Write pseudocode to explain how the task will be executed.
Create a For Loop using the range function.
Within this create an if...else statement. 
Use if to print where i is less than 6 and print the stars.
Use else to complete the star pattern.
Use parentheses for print function of else statement.
Use the print function to output the star pattern.
End'''

# The below variable named star has been initialised with the star symbol

star = "*"

for i in range(10):
    if i < 6:
        print(i * star)
    else:
        print((10 - i) * star)
    
    
# The for loop stipulates the range to be used.

# The if statement prints the first five stars.
        
# The else statement prints the rest.