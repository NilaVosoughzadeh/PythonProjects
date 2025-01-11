firstNumber = eval(input("Plz enter 1st number : "))
secondNumber = eval(input("Plz enter 2nd number : "))

print("----------------------")
print("+")
print("-")
print("/")
print("*")
print("-----------------------")

operation = input("Plz enter the operation sign : ")

if operation == "+":
    print(firstNumber + secondNumber)
elif operation == "-":
    print(firstNumber - secondNumber)
elif operation == "/":
    print(firstNumber / secondNumber)
elif operation == "//":
    print(firstNumber // secondNumber)
elif operation == "*":
    print(firstNumber * secondNumber)
else:
    print("Wrong Operation")