items = []

def add_item():
    new_item = input("Enter the item you want to add: ")
    items.append(new_item)
    print("ok so new item " + new_item + " added successfully. Updated list:")
    show_items()

def remove_item():
    if not items:
        print("The list is empty. There is nothing to remove.")
    else:
        print("This is the list again look at the list and state which item you want to remove: ")
        show_items()
        print("Enter the number of the item you want to remove: ")
        remove_index = int(input())
        if (remove_index > len(items)) or (remove_index < 1):
            print("Invalid number. Please enter a number between 1 and", len(items))
        else:
            removed_item = items.pop(remove_index - 1)
            print("ok so item " + removed_item + " removed successfully. Updated list:")
            show_items()

def show_items():
    if len(items) == 0:
        print("The list is empty.")
    else:
        print("The list is: ")
        for i in range(len(items)):
            print(i + 1, items[i])

print("Welcome to List Manager")
while True:
    print("What operation you want to perform? (Add / Remove)")
    print("1. Add")
    print("2. Remove")
    print("3. Show")
    print("4. Exit")
    print("Enter the option number (1, 2, 3 or 4): ")
    operation = input()
    if operation == "1":
        add_item()
    elif operation == "2":
        remove_item()
    elif operation == "3":
        show_items()
    elif operation == "4":
        print("Simply Lovely")
        break
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")