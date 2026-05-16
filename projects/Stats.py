def maxstats():
    print("What stats would you want to see of Max Verstappen")
    print("1. Championship")
    print("2. Wins")
    print("3. Podiums")
    print("4. Team")
    print("5. return to driver selection menu")
    choice2 = int(input("choice: "))
    if choice2 == 1:
        print("Championship = 4")
    elif choice2 == 2:
        print("Wins = 71")
    elif choice2 == 3:
        print("Podiums = 127")
    elif choice2 == 4:
        print("Team = Red Bull Racing")
    elif choice2 == 5:
        print("Returning to the driver selection menu")
        return
    else:
        print("Enter a Valid choice")

def lewstats():
    print("What stats would you want to see of Lewis Hamilton")
    print("1. Championship")
    print("2. Wins")
    print("3. Podiums")
    print("4. Team")
    print("5. return to driver selection menu")
    choice2 = int(input("choice: "))
    if choice2 == 1:
        print("Championship = 7")
    elif choice2 == 2:
        print("Wins = 105")
    elif choice2 == 3:
        print("Podiums = 203")
    elif choice2 == 4:
        print("Team = Ferrari")
    elif choice2 == 5:
        print("Returning to the driver selection menu")
        return
    else:
        print("Enter a Valid choice")

def sebstats():
    print("What stats would you want to see of Sebastian Vettel")
    print("1. Championship")
    print("2. Wins")
    print("3. Podiums")
    print("4. Team")
    print("5. return to driver selection menu")
    choice2 = int(input("choice: "))
    if choice2 == 1:
        print("Championship = 4")
    elif choice2 == 2:
        print("Wins = 53")
    elif choice2 == 3:
        print("Podiums = 122")
    elif choice2 == 4:
        print("Team = Aston Martin")
    elif choice2 == 5:
        print("Returning to the driver selection menu")
        return
    else:
        print("Enter a Valid choice")

def senstats():
    print("What stats would you want to see of Ayrton Senna")
    print("1. Championship")
    print("2. Wins")
    print("3. Podiums")
    print("4. Team")
    print("5. return to driver selection menu")
    choice2 = int(input("choice: "))
    if choice2 == 1:
        print("Championship = 3")
    elif choice2 == 2:
        print("Wins = 41")
    elif choice2 == 3:
        print("Podiums = 80")
    elif choice2 == 4:
        print("Team = McLaren")
    elif choice2 == 5:
        print("Returning to the driver selection menu")
        return
    else:
        print("Enter a Valid choice")

while(True):
    print("=== Welcome to F1 Driver Stats Program ===")
    print("Please choose the Drover whose stats you want to view please")
    print("1. Max Verstappen")
    print("2. Lewis Hamilton")
    print("3. Sebastian Vettel")
    print("4. Ayrton Senna")
    print("5. Exit")
    choice = int(input("So, What is your choice then??"))
    
    if choice == 1:
        maxstats()
    elif choice == 2:
        lewstats()
    elif choice == 3:
        sebstats()
    elif choice == 4:
        senstats()
    elif choice == 5:
        print("Simply Lovely")
        break
    else:
        print("Please enter a valid choice")