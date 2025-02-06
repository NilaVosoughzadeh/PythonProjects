hamburger = int(input("hamburger: "))
frenchFries = int(input("french Fries: "))
drink = int(input("drink :"))

hamburgerPrice = 5
frenchFriesPrice = 3
drinkPrice = 1

frenchFriesP = frenchFries * frenchFriesPrice
hamburgerP = hamburger * hamburgerPrice
drinkP = drink * drinkPrice
total = (hamburgerP) + (frenchFriesP) + (drinkP)

discount = total * 0.10

pay = total - discount

print(f"hamburger number : {hamburger} -> hamburger price : {hamburgerP}$")
print(f"frenchFries number : {frenchFries} -> frenchFries price : {frenchFriesP}$")
print(f"drinks number : {drink} -> drinks price : {drinkP}$")
print(f"total before discount: {total}$")
print(f"discount: {discount}$")
print(f"{pay}$")