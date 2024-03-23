'''Start
Create a file named alternative and save it as python in VS Code.
Create a variable alt_sen to ask the user to input a sentence.
Output using the print function.
Create the program logic using for loops
Use modulo for alternating letters.
use the split() and strip() methods to print each alternative word
as uppercase or lowercase
Use print to output the sentences.
End'''

# The variable alt_sen has been created.

# The input statement uses print to output.

alt_sen = str(input("Please enter a sentence:"))

# print(alt_sen)

alt_sentence = ""
for i, char in enumerate(alt_sen):

    if i % 2 == 0:
       alt_sentence  += char.lower()    
    else:
       alt_sentence  += char.upper()
print(alt_sentence) 

new_sentence = ""
words = alt_sen.split()  # Split the sentence into words

for i, word in enumerate(words):
    if i % 2 == 0:
        new_sentence += word.lower() + " "  # Make even-indexed words lowercase
    else:
        new_sentence += word.upper() + " "  # Make odd-indexed words uppercase

print(new_sentence.strip())  # Strip off any trailing whitespace before printing





      
      
  

     

     







    
















