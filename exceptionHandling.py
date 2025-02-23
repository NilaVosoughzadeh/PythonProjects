try:
    num = input("Enter number: ")
    print(num+3)

except NameError:
    print("Name Error!")
    #pass

except TypeError:
    print("Type Error")

print("Hi")