'''Start
Create a file named Library Management System.
Create dictionaries with key values.
Use a user defined checkout_book function.
Also use an if else function.
Call the checkout_book function with its parameters.
Create a user defined return_book function.
Within it use an if else function.
Use the print function to output.
End'''

# The below dictionaries show their key values


books_inventory = {'Book1': {'copies': 7, 'current_borrowers': []},
                   'Book2': {'copies': 4, 'current_borrowers': []}}

users_info = {'User1': {'borrowed_books': [], 'fines': 0},
              'User2': {'borrowed_books': [], 'fines': 0}}


# The below is a user defined function with it's parameters


def checkout_book(book_title, user_name):
    if books_inventory[book_title] ['copies'] > 0 and len(users_info[user_name]['borrowed_books']) < 3:
     books_inventory[book_title] ['copies'] -= 1
     books_inventory[book_title] ['current_borrowers'].append(user_name)
     users_info[user_name]['borrowed_books'].append(book_title)
     print(f"Book '{book_title}' checked out sucessfully.")
    else:
        print("Error: Book not available or user has reached the maximum borrow limit.")

checkout_book('Book1', 'User1')


# The below user defined function shows an if else statement in use


def return_book(book_title, user_name):
   if book_title in users_info[user_name]['borrowed_books']:
      books_inventory[book_title]['copies'] +=1
      books_inventory[book_title]['current_borrowers'].remove(user_name)
      users_info[user_name] ['borrowed_books'].remove(book_title)
      print(f"Book '{book_title}' returned successfully.")
   else:
      print("Error: User has not borrowed this book")
          