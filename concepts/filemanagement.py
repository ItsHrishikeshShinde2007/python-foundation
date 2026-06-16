import os

driver = input("PLease enter yoru favorite driver's name please: ")

# Write Mode Example
file = open("Favdriver.txt", "w")
file.write("Favorite Driver Report\n")
file.write("----------------------\n")
file.write("Driver Name: " + driver)
file.close()

# Append Mode Example
file = open("Favdriver.txt", "a")
file.write("\nTeam: Red Bull Racing")
file.close()

# Read Mode Example
file = open("Favdriver.txt", "r")
print(file.read())
file.close()

# Generate C++ File Example
file = open("test.cpp", "w")
file.write("""
#include<iostream>
using namespace std;
int main()
{
cout<<"Hello World\\n";
return 0;
}
""")
file.close()

file = open("test.cpp", "r")

# Read File Line By Line Example
for line in file:
    print(line)
file.close()

os.system("g++ test.cpp -o test")
os.system("./test")