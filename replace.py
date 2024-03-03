'''Start:
Create a file and name it replace.
Save it as python in a folder in VS Code.
Create a variable named sentence
Give it the value of "The!quick!brown!fox!jumps!over!the!lazy!dog!"
Use print function to see the sentence printed in python
Use another variable.
Then select the character in the sentence variable to be replaced.
Do this by putting it into the .replace function with it's replacement.
Then use the print function to print the new variable and see the changes.
Change the modified sentence further to make it uppercase.
Use the .upper function with this new sentence variable.
Use the print function to see the sentence change to uppercase.
Change the sentence again to print in reverse by using slicing.
State the start and end of the letters to be printed.
Use[:: -1]
Use the print function to see the sentence printed in reverse.
End '''

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

print(sentence)

# The!quick!brown!fox!jumps!over!the!lazy!dog!

replace_in_sentence = sentence.replace( "!", " ")

print(replace_in_sentence)

# The quick brown fox jumps over the lazy dog

uppercase_sentence = replace_in_sentence.upper( )

print(uppercase_sentence)

# THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

reverse_sentence = uppercase_sentence[::-1]

print(reverse_sentence)

# GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT