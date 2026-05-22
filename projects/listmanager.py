Listmanager = []
print("Welcome to List manager app")
while(True):
    print("Choose from the below")
    print("a. Add a Task")
    print("b. Delete a completed task")
    print("c. List all the task")
    print("d. Exit")
    choice = input("")
    if(choice == 'a'):
        task = str(input("State the task that you want to add: "))
        Listmanager.append(task)
        print()
    elif(choice == 'b'):
        if(len(Listmanager) == 0):
            print("There are no tasks to list")
        else:
            for i in range(len(Listmanager)):
                print("Task " , i + 1 ,":", Listmanager[i])
            print()
            delindex = int(input("Please State task number that you want to delete:"))
            if(delindex < 1 or delindex > len(Listmanager)):
                print("The Task does not exists")
            else:
                print("Ok so the task " + Listmanager[delindex - 1] + " is deleted")
                Listmanager.pop(delindex - 1)
                print()
                print("The revised list is:- ")
                for i in range(len(Listmanager)):
                    print("Task " , i + 1 ,":", Listmanager[i])
            print()
    elif(choice == 'c'):
        if(len(Listmanager) == 0):
            print("No list in the To do list to show")
        else:
            print("The List of all the tasks are:-")
            for i in range(len(Listmanager)):
                 print("Task " , i + 1 ,":", Listmanager[i])
        print()
    elif(choice == 'd'):
        print("Simply lovely")
        break
    else:
        print("Invalid Choice")