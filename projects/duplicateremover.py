def listdrivers():
    for i in range(len(drivers)):
        print(i + 1, drivers[i])

def add_driver():
    print("The list of drivers is stated again who else would you like to add in the list and where?")
    listdrivers()
    new_driver = input("Enter the name of the driver you want to add: ")
    if new_driver in drivers:
        print("This driver is already in the list. Please enter a different driver.")
    else:
        drivers.append(new_driver)

def remove_driver():
    print("This is the list again look at the list and state which driver you want to remove: ")
    listdrivers()
    print("Enter the number of the driver you want to remove: ")
    remove_index = int(input("Enter the number of the driver you want to remove: "))
    if (remove_index > len(drivers)) or (remove_index < 1):
        print("Invalid number. Please enter a number between 1 and", len(drivers))
    elif(remove_index == 1):
        print("Haha nice try but you can't remove Max, he is the best driver in the world and he deserves to be on top")
    else:
        removed_driver = drivers.pop(remove_index - 1)
        print("ok so driver " + removed_driver + " removed successfully. Updated list of drivers:")
        listdrivers()

drivers = ["Max verstappen", "Kimi Antonelli", "Charles Leclerc", "Oscar Piastri", "Lando Norris"]
print("Ok so this is the list of drivers which i feel are the best in the world right now")
listdrivers()
while True:
        print("What operation you want to perform?")
        print("1. Add")
        print("2. Remove")
        print("3. List")
        print("4. Exit")
        print("Enter the option number (1, 2, 3 or 4): ")
        operation = input()
        if operation == "1":
            add_driver()
        elif operation == "2":
            remove_driver()
        elif operation == "3":
            print("The list of drivers is: ")
            listdrivers()
        elif operation == "4":
            print("Simply Lovely")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")