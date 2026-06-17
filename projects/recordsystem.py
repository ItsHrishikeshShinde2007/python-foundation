drivers =[
    {
        "Name" : "Max Verstappen",
        "Racing Team" :  "Red Bull Racing",
        "Number" : 1
    },
    {
        "Name" : "Charles Leclerc",
        "Racing Team" : "Scuderia Ferrari",
        "Number" : 16
    },
    {
        "Name" : "Fernando Alonso",
        "Racing Team" : "Aston Martin Formula 1",
        "Number" : 14
    },
]

def viewdrivers():
    for i in range (len(drivers)):
        print(f"Driver Number :", i + 1)
        for key, value in drivers[i].items():
            print(key, ":" ,value)
        print()

def addnewdriver():
    newdriver = {}
    newdriver["Name"] = input("Enter the driver's name:")
    newdriver["Racing Team"] = input("Please enter his Racing team:")
    newdriver["Number"] = int(input("Please the driver's racing number:"))
    drivers.append(newdriver)
    viewdrivers()

def deletedriver():
    viewdrivers()
    deldriver = int(input("Ok so enter the driver number that you want to delete: "))
    if(deldriver == 1):
        print("Haha Nice try but no you cant take that out from there mate!")
    elif(deldriver < 1 or deldriver > len(drivers)):
        print("No driver at index", deldriver)
    else:
        print("Ok driver " + drivers[deldriver - 1]["Name"] + " is selected")
        print("Are you sure you weant to delete " + drivers[deldriver - 1]["Name"] + " ?")
        choice = input("Yes or No ('Y'/'N')")
        if option.lower() == "y":
            drivers.pop(deldriver - 1)
            print("Revised list is:- ")
            viewdrivers()
        elif option.lower() == "n":
            print("Ok cencellation proces of driver " + drivers[deldriver - 1]["Name"])
            print("The list is: ")
            viewdrivers()
        else:
            print("That was a wrong choice")
            print("Enter a 'Y' or 'y' to delete")
            print("Enter a 'N' and 'n' to cancel the delete")

def searchdriver():
    dname = input("Enter the name of the driver that you are searching:- ")
    driverfound = False
    for driver in drivers:
        if (driver["Name"].lower() == dname.lower()):
            driverfound = True
            print("Driver found!!!")
            for key, value in driver.items():
                print(key, ":" , value)
            print()
    if(driverfound == False):
        print("Driver does not exist")

print("List of some of my favorite drivers are:")
viewdrivers()
while(True):
    print("Choose from the following options")
    print("a. Add")
    print("b. Delete")
    print("c. Search")
    print("d. View list")
    print("e. Exit")
    option = (input(""))
    if option.lower() == "a":
        addnewdriver()
    elif option.lower() == "b":
        deletedriver()
    elif option.lower() == "c":
        searchdriver()
    elif option.lower() == "d":
        viewdrivers()
    elif option.lower() == "e":
        print("Simply Lovely")
        break
    else:
        print("Please choose a, b, c, d or e")