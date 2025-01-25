# 1- برنامه ای بنویسید که حاصل جمع اعداد یک تا 100 را حساب کند
sum = 0
for i in list(range(1, 101)) :
    sum+=i
print(sum)

# 2- برنامه ای بنویسید که حاصل جمع اعداد فرد 1 تا 100 را حساب کند.
sum=0
for i in list(range(1,101,2)):
    sum+=i
print(sum)

# 3- برنامه ای بنویسید که عدد a,b را از ورودی بگیرد و سپس حاصل جمع اعداد a تا b را حساب کند.s = int(input("Enter Number: "))
a = int(input("Enter : "))
b = int(input("Enter : "))
sum=0
for i in list(range(a,b+1)):
    sum+=i

print(sum)