ticket = int(input("Enter ticket: "))
if ticket<=90 :
    print("No ticket")
elif ticket>=91 and ticket<=110 :
    print("Small ticket")
elif ticket>=111 :
    print("Big ticket")
else :
    print("Woh")