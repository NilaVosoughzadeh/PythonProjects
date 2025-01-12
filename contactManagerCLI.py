print("=========Main Menu=========")
print("1-Create new contact")
print("2-Edit")
print("3-Delete")
print("4-Search")
print("5-Show Contacts")
print("6-Exit")

#Dictionary (Data structure)
contacts = {}

while True :
    item = input("Choose item number: ")

    match item :

        case"1":
            name = input("Enter Name: ").lower()

            if name in contacts.keys():
                print("This name already exists")

            else:
               phone = input("Enter phone number: ")
               contacts[name] = phone
               print(f"contact {name} successfuly created")

        case"2":
            print("1- Edit name")
            print("2-Edit phone")

            itemEdit = input("Choose item: ")

            if itemEdit == "1" :
                name = input("Enter the name you want to edit: ").lower()

                if name in contacts.keys():
                    newName = input("Enter new name: ").lower()
                    contacts[newName] = contacts[name]
                    del contacts[name]
                    print(f"Name changed to {newName}")
                else:
                    print(f"{name} doesn't exist")

            elif itemEdit == "2":
                name = input("Enter the name you want to edit phone number:").lower()
                if name in contacts.keys():
                    newPhone = input("Enter new phone number: ")
                    contacts[name] = newPhone
                    print(f"Phone number {name} : {newPhone}")
                else:
                    print(f"{name} doesn't exist!")
        
        case "5":
            print(contacts)