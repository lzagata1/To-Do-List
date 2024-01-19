#To-Do List pt2
#1/17/24
#Litzy

#initialize
groceryList = ["milk","eggs","bread","apples","chocolate","spinach","butter"]

#functions 
def menu():
    #Code that runs each calculation goes here
    print("Please choose an option: (Type in a number between 1-8)")
    print("1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list \n5. Exit the program \n6. Remove all the tasks from the to do list \n7. sort the list alphabetically \n8. print the number of items on the to do list ")
    option = int(input("Option: "))
    if option == 5:
        quit()

    if option == 1:
        task = input("What task would you like to add? ")
        groceryList.insert(7, task)
        print(groceryList)
    elif option == 2:
        print(groceryList)
    elif option == 3:
        complete = input("What task did you complete? ")
        i = groceryList.index(complete) 
        groceryList[i] = complete + " [X]"
        -print(groceryList)
    elif option == 4:
        remove = input("What task would you like to remove? ")
        groceryList.remove(remove)
        print(groceryList)
    elif option == 5:
        groceryList.clear()
        print(groceryList)
    elif option == 6:
        groceryList.sort()
        print(groceryList)
    elif option == 7: 
        print(len(groceryList))


menu()