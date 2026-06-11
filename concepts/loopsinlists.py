drivers = ["Lando Norris", "Max Verstappen", "Oscar Piastri"]

print("Ok so there are simpley two ways how to can print the list of drivers, one is using for loop and other is using while loop")
print("Using for loop: ")
for i in range(len(drivers)):
    print(i + 1, drivers[i])
print("Using while loop: ")
i = 0
while i < len(drivers):
    print(i + 1, drivers[i])
    i += 1
print("Or if you are feeling lazy you can simply print the list without any loop: ")
print(drivers)
print("But this is not a good way to print the list because it will not look good and it will not be easy to read, so it is better to use for loop or while loop to print the list in a more presentable way")
print("If you want to print only the driver names without the index then you can simply use for loop like this: ")
for driver in drivers:
    print(driver)
print("But if you want to print the list in a more presentable way then you can use for loop or while loop and print the index and the driver name in a nice format")
