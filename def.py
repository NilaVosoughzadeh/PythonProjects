# def helloWorld():
#     print("Hello World")
# helloWorld()

def helloWorld():
     return "helloWorld"
print(helloWorld())

# a = int(input("Enter num1 : "))
# b = int(input("Enter num2 : "))
# def sum(a , b):
#      return a + b
# print(sum(a , b))

def num(rangeNum):
     for i in range(1 , rangeNum+1):
          print(i , end="  ")
num (10)

print("")


# num = input("Enter: ")
# def sum(num):
#      sum = 1
#      for i in range(1 , num+1):
#           sum = sum * i 
#      return sum
# print(sum(10))

list = [1,2,3,4,6]
def count():
     c = 0
     for num in list:
          if num % 2 == 0:
               c += 1
     return c
print(count)