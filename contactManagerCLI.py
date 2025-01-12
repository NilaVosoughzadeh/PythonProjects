from colorama import Fore

print(Fore.YELLOW)

print("======Menu======")
print("1) Create new contact")
print("2) Edit")
print("3) Delete")
print("4) Search")
print("5) Show Contacts")
print("6) Exit")

print(Fore.RESET)

#Dictuinary (Data Structure)
contacts = {}

while True :
    item = input("Choose item number: ")

    match item :

        case"1":
            print(Fore.RED)
            name = input("Enter Name: ").lower()

            if name in contacts.keys():
                print("This name already existed")

            else:
               phone = input("Enter phone number: ")
               contacts[name] = phone
               print(f"contact {name} successfuly created")
               print(Fore.RESET)

        case"2":
            print(Fore.CYAN)
            print("1- Edit name")
            print("2- Add phone to an existing contact")

            itemEdit = input("Choose item: ")

            if itemEdit == "1" :
                name = input("Enter the name you want to edit: ").lower()

                if name in contacts.keys():
                    newName = input("Enter new name: ").lower()
                    contacts[newName] = contacts[name]
                    del contacts[name]

                else:
                    print(f"{name} doesn't exist")

            elif itemEdit == "2" :
                name = input("Enter the name you want to add: ").lower()
                if name in contacts.keys():
                    newPhone = newPhone = input("Enter new name: ").lower()
                    contacts[name].append(newPhone)

                else:
                    print(f"{name} doesn't exist")
            print(Fore.RESET)
                    
        case"3":
            print(Fore.MAGENTA)
            nameDel = input("Enter the name you want to delete: ")

            if nameDel in contacts.keys():
                del contacts[nameDel]
                print(f"{nameDel} Deleted")

            else:
                print(f"{nameDel} not found!")
            print(Fore.RESET)

        case"4":
            print(Fore.LIGHTGREEN_EX)
            find = input("Enter the name you want to find : ")

            if find in contacts.keys():
                print(contacts[find])
            else:
                print(f"{find} not found!")
            print(Fore.RESET)

        case"5":
            print(Fore.LIGHTBLUE_EX)
            print(contacts)
            print(Fore.RESET)

        case"6":
            print(Fore.LIGHTRED_EX)
            print("Good Luck!!")
            break
            print(Fore.RESET)