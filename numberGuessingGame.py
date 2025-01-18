from random import randint
number = randint(1,10)
counter = 0
while counter < 5 :
    guess = eval(input("Enter number: "))
    if guess == number :
        print("That's right! Congrats")
        break
    elif guess < number :
        print("Select higher number")
    else :
        print("Select lower")
    counter += 1
print("The number was : " , number)