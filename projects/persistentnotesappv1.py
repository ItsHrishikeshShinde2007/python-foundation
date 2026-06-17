def addnote():
    print("You have choosen to add a note")
    note = input("Please add a note: ")
    file = open("notes.txt", "a")
    file.write(note + "\n")
    file.close()
    print()

def viewnote():
    i = 1
    file = open("notes.txt", "r")
    for notes in file:
        print(f"{i} . {notes.strip()}")
        i = i + 1
    if i == 1:
        print("No notes found")
    print()
    file.close()

def clearnotes():
    print("notes have been successfully cleared")
    file = open("notes.txt", "w")
    file.write("")
    file.close()

while(True):
    print("==== Persistent Notes Application ====")
    print("Please choose from below")
    print("a. Add a note")
    print("b. View notes")
    print("c. clear all notes")
    print("d. Exit")
    choice = input("Please input your choice: ")
    if(choice.lower() == 'a'):
        addnote()
    elif(choice.lower() == 'b'):
        viewnote()
    elif(choice.lower() == 'd'):
        print()
        print("Simply lovely")
        break
    elif(choice.lower() == 'c'):
        clearnotes()
    else:
        print("That was a wrong choice")
        print("Enter a 'A' or 'a' to add notes")
        print("Enter a 'B' and 'b' to not view notes")
        print("Enter a 'C' or 'c' to exit")