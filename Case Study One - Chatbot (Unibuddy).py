'''Start:
Create a file named Case Study One-Chatbot(Unibuddy)
Save it as a python file in VS Code.
Write out pseudocode to explain the case study steps.
Create three seperate input statements.
Ask for the users name, favourite colour and age.
Use the print function to output.
For favourite user colour and age, create if ..else statements.
From the output for each, create personalised greetings.
Use an f string to concatenate and create a sentence.
Create feature where user can ask questions.
Use the if, elif, else statement control structure.
Use the print function to output these.
End'''


user_name = input("Please can you enter your name: ")

print(user_name)

print(f"Hi {user_name}")

# The f string is used to concatenate


fav_color = input("Please can you enter your favourite colour: ")

print(fav_color)

print(f"Your favourite colour is {fav_color}.")

if fav_color == "blue":
    print("Why don't you join the Blue Art Club?")
else:
    print("We have lots of colour inspired clubs that you can join on campus.")


user_age = int(input("Please can you enter your age: "))

print(user_age)

print(f"Your age is {user_age}")

if user_age == 18:
    print("Why don't you check out our freshmen specific events?")
else:
    print("Why don't you check out our university events?")


# The if...else statement provides the user with age related information


user_question = input("Please enter a specific question: ")

print(user_question)

if user_question == "Where is the library?":
   print("It is behind the sports center")
elif user_question == "Where is the gym?":
   print("It is to the right of the main building")
elif user_question == "Where is the politics lecture room?":
   print("It is opposite the psychology project meeting room")
else:
   print("Please enter another question")

# The above if,elif,else enables the user to ask specific questions and recieve a response


   








