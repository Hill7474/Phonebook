print("Welcome to the phone book!")

# Let's create an empty dictionary to store our entries in
phonebook_dict = {}

# Repeat this loop until they exit
while True:
    # Print the menu options
    print("What would you like to do?")
    print("    1 - Add an entry")
    print("    2 - Lookup an entry")
    print("    3 - Delete an entry")
    print("    4 - Exit")
    choice = input("Enter an option: ")
    if choice == '1':
        name = input('Name: ')
        phone = input('Telephone Number: ')
        book[name] = phone
    elif choice == '2':
        name = input('Name: ')
      
        print("Their number is:", book[name])
    elif choice == '3':
        name = input('Name: ')
        # This will also cause a KeyError if name is not a key
        del book[name]
    elif choice == '4':
        # exit the loop
        break
    else:
        print('Invalid option.')
