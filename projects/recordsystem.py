print("List of some of my favorite drivers are:")
drivers = [
    {
        "Name" : "Max Verstappen",
        "Racing Team" :  "Red Bull Racing",
    },
    {
        "Name" : "Charles Leclerc",
        "Racing Team" : "Scuderia Ferrari",
    },
    {
        "Name" : "Fernando Alonso",
        "Racing Team" : "Aston Martin Formula 1",
    },
]
for i in range (len(drivers)):
    print(f"Driver Number :", i + 1)
    for key, value in drivers[i].items():
        print(key, ":" ,value)
    print()
while(True):
    print("Choose from the following options")
    print("a. Add")
    print("b. Delete")
    print("c. Search")
    print("d. Exit")
    option = (input(""))
    if(option == "A" or option == "a"):
        newdriver = {}
        newdriver["Name"] = input("Enter the driver's name:")
        newdriver["Racing Team"] = input("Please enter his Racing team:")
        drivers.append(newdriver)
        for i in range (len(drivers)):
            print(f"Driver Number :", i + 1)
            for key, value in drivers[i].items():
                print(key, ":" ,value)
            print()
    elif(option == "B" or option == "b"):
        deldriver = int(input("Ok so enter the driver number that you want to delete: "))
        if(deldriver == 1):
            print("Haha Nice try but no you cant take that out from there mate!")
        elif(deldriver > len(drivers)):
            print("No driver at index", deldriver)
        else:
            print("Ok driver " + drivers[deldriver - 1]["Name"] + "is deleted")
            drivers.pop(deldriver - 1)
            print("Revised list is:- ")
            for i in range (len(drivers)):
                print(f"Driver Number :", i + 1)
                for key, value in drivers[i].items():
                    print(key, ":" ,value)
                print()            
    elif(option == "C" or option == "c"):
        dname = input("Enter the name of the driver that you are searching:- ")
        driverfound = False
        for driver in drivers:
            if (driver["Name"] == dname):
                driverfound = True
                print("Driver found!!!")
                for key, value in driver.items():
                    print(key, ":" , value)
                print()
        if(driverfound == False):
            print("Driver does not exist")
    elif(option == "D" or option == "d"):
        print("Simply Lovely")
        break
    else:
        print("That was a wrong choice")
        print("Enter a 'Y' or 'y' to add")
        print("Enter a 'N' and 'n' to not add")