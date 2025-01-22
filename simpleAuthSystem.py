user = input("Enter your username: ")
passw = input("Enter your password: ")

print("Welcome to our website , Now please login!")

username = input("Enter username: ")
password = input("Enter password: ")

if username == user and password == passw :
    print("Welcome")
else :
    print("Invalid input")



users = {
    "nila" : 1384 ,
    "arash" : 1390 ,
    "vania" : 1388
}
enterUser = input("Enter username: ")
enterPass = int(input("Enter password: "))
# if enterUser in users and users[enterUser] == enterPass :
#     print("You are our user!")
# else :
#     print("Sorry I don't know you :(")
while enterUser not in users and users[enterUser] != enterPass :
    print("Your username or pass is wrong!")
    enterUser = input("Enter username: ")
    enterPass = int(input("Enter password: "))
print("You logged in")