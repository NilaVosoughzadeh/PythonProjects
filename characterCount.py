name = input("Enter your fullname: ").lower().strip().replace(" ","")
case = []
for n in name :
    if n not in case :
        print(f"your name has {name.count(n)} -> {n}")
        case.append(n)