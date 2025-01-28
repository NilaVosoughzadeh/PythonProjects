from random import randint
from colorama import Fore

x = "y"

while x == "y":
    number = randint(1,6)

    if number == 1:
        print(Fore.LIGHTRED_EX)
        print("===========")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("===========")
        print(Fore.RESET)

    elif number == 2:
        print(Fore.LIGHTYELLOW_EX)
        print("===========")
        print("|         |")
        print("|  0   0  |")
        print("|         |")
        print("===========")
        print(Fore.RESET)

    elif number == 3:
        print(Fore.LIGHTMAGENTA_EX)
        print("===========")
        print("|       0 |")
        print("|    0    |")
        print("| 0       |")
        print("===========")
        print(Fore.RESET)

    elif number == 4:
        print(Fore.LIGHTGREEN_EX)
        print("===========")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("===========")
        print(Fore.RESET)

    elif number == 5:
        print(Fore.LIGHTCYAN_EX)
        print("===========")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("===========")
        print(Fore.RESET)

    elif number == 6:
        print(Fore.LIGHTBLUE_EX)
        print("===========")
        print("| 0  0  0 |")
        print("|         |")
        print("| 0  0  0 |")
        print("===========")
        print(Fore.RESET)

    x = input("Do you want to continue? ")

    if x == "yes":
        continue
    else:
        break