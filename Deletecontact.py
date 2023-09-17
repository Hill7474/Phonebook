
def remove_existing(pb):
    # This function is to remove a contact's details from existing phonebook
    query = str(
        input("Please enter the name of the contact you wish to remove: "))
    # We'll collect name of the contact and search if it exists in our phonebook
     
    temp = 0
    # temp is a checking variable here. We assigned a value 0 to temp.
     
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            # Temp will be incremented & it won't be 0 anymore in this function's scope
             
            print(pb.pop(i))
            # The pop function removes entry at index i
             
            print("This query has now been removed")
            # printing a confirmation message after removal.
            # This ensures that removal was successful.
            # After removal we will return the modified phonebook to the calling function
            # which is main in our program
             
            return pb
    if temp == 0:
        # Now if at all any case matches temp should've incremented but if otherwise,
        # temp will remain 0 and that means the query does not exist in this phonebook
        print("Sorry, you have entered an invalid query.\
    Please recheck and try again later.")
         
        return pb