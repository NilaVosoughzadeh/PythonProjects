num = int(input("Enter num ppl: "))
contacts = {}
for n in range(num):
    name = input(f"Enter name {n}: ")
    phone = input(f"Enter phone {n}: ")
    contacts[name] = phone
print(contacts)