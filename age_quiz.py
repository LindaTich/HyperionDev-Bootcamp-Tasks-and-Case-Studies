'''Start:
Create a file named age_quiz.
Save as a python file in a folder in VS Code.
Create a variable named age.
Use input to ask user to enter their age.
Use print to output age.
Use if to show if anyone is 100 or over.
Then use print fuction to output "Sorry you're dead".
Use elif to show if anyone is 65 or over.
Then use print function to output"Enjoy your retirement!".
Use elif to show if anyone is 40 or over.
Then use print function to output "You're over the hill"
Use elif to show if anyone 13 or under.
Then use print to output "You qualify for the kiddie discount".
Use elif to state if user is 21.
Then use print function to output "Congrats on your 21st!".
Use else to show any other age.
Then use print function to output "Age is but a number".
End'''

age = int(input("Please enter your age: "))

print(age)

if age >= 100:
     print("Sorry you're dead")
elif age >= 65:
     print("Enjoy your retirement!")
elif age >= 40:
     print("You're over the hill")
elif age == 21:
     print("Congrats on your 21st!")
elif age <= 13:
     print("You qualify for the kiddie discount")
else:
     print("Age is but a number")


 # The above if else statement is now in logical order.  
 
 # I have left white space in between the code to make the code easier to read.  