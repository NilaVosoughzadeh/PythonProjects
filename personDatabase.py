file = open("data.txt" , "a")

name = input("Enter name: ")
lName = input("Enter last name: ")
age = int(input("Enter age: "))
file.write(f"{name} - {lName} - {age} \n")

file.close()