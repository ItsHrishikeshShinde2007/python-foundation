import math
def sign(value):
    if(value % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def state(value):
    if(value > 0):
        print("Number is Positive")
    elif(value < 0):
        print("Number is Negative")
    else:
        print("The number is 0")

def divisibilityby5(value):
    print("Let's see if it is divisible by 5?")
    if(value % 5 == 0):
        print("Yes, this is divisible by 5")
    else:
        print("No, this is not divisible by 5")

def primechecker(value):
    print("Number is: ", value)
    if value <= 1:
        print("Not a prime number")
    else:
        is_prime = True
        for i in range(2, int(value**0.5) + 1):
            if value % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime number")
        else:
            print("Not a prime number")
def perfectsquare(value):
    if(value >= 0):
        root = math.sqrt(value)

        if root == int(root):
            print("The value is a perfect square")

        else:
            print("The value is not a perfect square")



while True:
    value = int(input("please enter the number: "))
    print("1. Odd or even")
    print("2. Positive or negative")
    print("3. Divisible by 5 or no")
    print("4. Is a Perfect square or not")
    print("5. Check whether prime or not")
    print("6. End")
    choice = int(input("Choose among the things to check"))
    if choice == 1:
        sign(value)
    elif choice == 2:
        state(value)
    elif choice == 3:
        divisibilityby5(value)
    elif choice == 4:
        perfectsquare(value)
    elif choice == 5:
        primechecker(value)
    elif choice == 6:
        print("Exiting Number Analyzer...")
        break
    else:
        print("please try again")