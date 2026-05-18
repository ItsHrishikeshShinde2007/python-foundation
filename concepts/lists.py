drivers = ["Max Verstappen", "Kimi Antonelli", "Charles Leclerc", "Oscar Piastri", "Lando Norris"]
while(True):
    print("Ok so the current GOAT on the grids are ", drivers)
    print("Would you like to add or delete something")
    print("1. Yes")
    print("2. No")
    answer = int(input(""))
    if(answer == 1):
        print("Please specify if you want to add or delete the drivers")
        print("1. Add")
        print("2. Delete")
        answer2 = int(input(""))
        if(answer2 == 1):
            new_name = str(input("Please State the name of the driver: "))
            new_index = int(input("Please state where would you want to put him: "))
            if(new_index == 0):
                print("Nah Nah Nah no one takes his place he is the real Goat try any another index you ain't getting that one")
            else:
                drivers.insert(new_index, new_name)
                print("Ok so the Updates list is: ", drivers)
        if(answer2 == 2):
            print("Alright, state the index of the driver that you want to remove below")
            answer3 = int(input("But remember, you can't remove the real GOAT from the list: "))
            if(answer3 == 0):
                print("Haha Nice try but nah that ain't happening, he is a goat for a reason and that's why he is up there, why dont you try removing Lando? ")
            else:
                print("Ok so you have choosen driver ", drivers[answer3] ," from the list you sure want to delete this driver?")
                print("1. Yes")
                print("2. No")
                answer4 = int(input(""))
                if(answer4 == 1):
                    print("alright,", drivers[answer3], "removed from the list")
                    drivers.pop(answer3)
                    print("Ok so the Updates list is: ", drivers)
                else:
                    print("Ok deleting driver ", drivers[answer3], " from Goat series cancelled")
                    print("So the list stays: ", drivers)
    elif(answer == 2):
        print("Fair I know I am the best to rank the top drivers")
        print("The list is: ", drivers)