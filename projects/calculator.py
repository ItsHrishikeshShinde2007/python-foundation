print("Simple Calculator")

a = float(input("Enter first number: "))
c = str(input("Enter operator (+, -, *, /, ^, //): "))
b = float(input("Enter second number: "))

if c == "+":
    print (a + b)
elif c == "-":
    print (a - b)
elif c == "*":
    print (a * b)
elif c == "/":
    if b == 0:
        print ("Error division by zero")
    else:
        print (a / b)
elif c == "^":
    print (a ** b)
elif c == "//":
    if b == 0:
        print ("Error division by zero")
    else:
        print (a // b)
else:
    print ("Invalid operator, please try again like (a + b) or (a - b)")