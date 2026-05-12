x = int(input("Rate Max Verstappen out of 10: "))
y = int(input("Rate Lewis Hamilton out of 10: "))

if x == y:
    print("Okay so you rate them the same, I see")
else:
    print("You rated them differently, thats interetsing let's see how you rated them")

if x > 0:

    if x > 8:
        print(f"ok so you rated max {x}, thats lovely. I am sure we can be good friends")
    else:
        print("nope that is way too low, do you even watch F1?")

elif x < 0:
    print("Just get out mate you deserve to be banned from this planet")

else:
    print("You are just crazy if you rate him 0")

if x > 0 and y > 0:
    print("Both the rates are positive, you are a good man, you have my respect")
elif x > 0 or y > 0:
    print("So, you rate only one of them positive, let's see how you rated them")
    if x > y:
        print("and i see we are gonna be good friends max verstappen all the way to world championship")
    elif y > x:
        print("and honestky i am sorry mate you and me, we are on different sides")
    else:
        print("Ok as long as you rate both of them the same, we are good")
else:
    print("Ok talking to you was a waste of time then")