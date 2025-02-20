# w = write  , r = read  , a = append

file = open("file.txt" , "r")
readFile = file.read()
print(readFile.split("\n"))

# for i in readFile:
#     if i == "Nila":
#         count = count + 1
#         print(count)


new = open("new.txt" , "w")
new.write("Hello World!")
new.close()

# database = open("database.txt" , "a")
# text = input("Enter sth: ")
# database.write(f"\n{text}")
# database.close()
#database.remove()