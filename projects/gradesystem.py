def gradesystem(points):
    if(points > 100 or points < 0):
        print("Invalid Choice")
    elif(points >= 90):
        print("Dominance just like Verstappen")
    elif(points >= 80):
        print("Still a contender")
    elif(points >= 60):
        print("Podium Finisher")
    elif(points >= 40):
        print("Midfeild")
    elif(points >= 0):
        print("Disaster Class")

points = float(input("Enter your marks please (0 - 100): "))
gradesystem(points)