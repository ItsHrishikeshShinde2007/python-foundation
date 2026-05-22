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

option = (input("Wanna add your favorite driver?(Y/N)"))
if(option == "Y" or option == "y"):
    newdriver = {}
    newdriver["Name"] = input("Enter the driver's name:")
    newdriver["Racing Team"] = input("Please enter his Racing team:")
    drivers.append(newdriver)
    for i in range (len(drivers)):
        print(f"Driver Number :", i + 1)
        for key, value in drivers[i].items():
            print(key, ":" ,value)
        print()
elif(option == "N" or option == "n"):
    print("Ok I know my taste in choosing the best driver is so good.")
else:
    print("That was a wrong choice")
    print("Enter a 'Y' or 'y' to add")
    print("Enter a 'N' and 'n' to not add")