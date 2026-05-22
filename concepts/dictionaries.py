print("My favorite F1 driver is: ")

myfavdriver1 = {
    "Name" : "Max Verstappen",
    "Racing Team" : "Red Bull Racing",
    "World Championship" : 4,
}

for key, value in myfavdriver1.items():
    print(key, ":" ,value)

YorN = input("Do you also wanna create a dictionary by inputing your favorite driver details in (Y/N)?")
if (YorN == "Y" or YorN ==  "y"):
    myfavdriver2 = {}
    myfavdriver2["Name"] = input("Enter driver name: ")
    myfavdriver2["Racing Team"] = input("Enter his racing team name: ")
    myfavdriver2["Driver Number"] = int(input("Enter his driver number: "))
    print("Ok so your favorite Driver is:-")
    for key, value in myfavdriver2.items():
        print(key, ":" ,value)
elif (YorN == "N" or YorN == "n"):
    print("Fine")
else:
    print("Alright nevermind")