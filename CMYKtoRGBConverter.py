cyan = float(input("Cyan: "))
magenta = float(input("Magenta: "))
yellow = float(input("Yellow: "))
black = float(input("Black: "))

red = 255 * (1 - cyan) * (1 - black)
green = 255 * (1 - magenta) * (1 - black)
blue = 255 * (1 - yellow) * (1 - black)

print(f"RGB Values: R={red}, G={green}, B={blue}")