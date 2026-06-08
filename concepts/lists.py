def listdrivers():
    for i in range(len(drivers)):
        print(i + 1, drivers[i])

drivers = ["Max verstappen", "Kimi Antonelli", "Charles Leclerc", "Oscar Piastri", "Lando Norris"]
print("Ok so this is the list of drivers which i feel are the best in the world right now")
listdrivers()

while True:
        print("What operation you want to perform? (Add / Remove)")
        print("1. Add")
        print("2. Remove")
        print("3. Show")
        print("4. Exit")
        print("Enter the option number (1, 2, 3 or 4): ")
        operation = input()
        if operation == "1":
            print("The list of drivers is stated again who else would you like to add in the list and where?")
            listdrivers()
            new_driver = input("Enter the name of the driver you want to add: ")
            new_driver_position = int(input("Enter the position where you want to add the driver: "))
            if (new_driver_position > len(drivers) + 1) or (new_driver_position < 1):
                print("Invalid position. Please enter a position between 1 and", len(drivers) + 1)
            elif(new_driver_position == 1):
                print("Haha nice try but you can't add any other driver to top, Max is the best driver in the world and he deserves to be on top")
            else:
                drivers.insert(new_driver_position - 1, new_driver)
                print("ok so new driver " + new_driver + " added successfully. Updated list of drivers:")
                listdrivers()
        elif operation == "2":
            print("This is the list again look at the list and state which driver you want to remove: ")
            listdrivers()
            print("Enter the number of the driver you want to remove: ")
            remove_driver = int(input("Enter the number of the driver you want to remove: "))
            if (remove_driver > len(drivers)) or (remove_driver < 1):
                print("Invalid number. Please enter a number between 1 and", len(drivers))
            elif(remove_driver == 1):
                print("Haha nice try but you can't remove Max, he is the best driver in the world and he deserves to be on top")
            else:
                removed_driver = drivers.pop(remove_driver - 1)
                print("ok so driver " + removed_driver + " removed successfully. Updated list of drivers:")
                listdrivers()
        elif operation == "3":
            print("The list of drivers is: ")
            listdrivers()
        elif operation == "4":
            print("Simply Lovely")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")