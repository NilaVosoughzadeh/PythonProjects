import os
import subprocess

# Find text file and print
result = subprocess.check_output('dir /S /B *.txt' , shell=True).decode(errors="replace").split()
print(result)

replacementCode = {
    "a" : "@" ,
    "b" : "8" ,
    "c" : "(" ,
    "d" : "6" ,
    "e" : "3" ,
    "h" : "#" ,
    "i" : "!" ,
    "k" : "<" ,
    "l" : "|" ,
    "m" : "^^" ,
    "n" : "^" ,
    "o" : "0" ,
    "s" : "$" ,
    "t" : "+" ,
    "z" : "7"
}

def encryptText(text) :
    encryptedTxt = ""
    for i in text :
        encryptedTxt += replacementCode.get(i.lower() , i)
    return encryptedTxt

# Read original file
originalFile = open("form.txt" , "r")
text = originalFile.read()
lines = text.splitlines()

encryptLines = []
for line in lines :
    words = line.split()
    encryptWords = []
    for word in words :
        encryptWord = encryptText(word)
        encryptWords.append(encryptWord)
    encryptLines.append(" ".join(encryptWords))


backupFile = open("backupForm.txt" , "w")
for line in encryptLines :
    backupFile.write(line + "\n")

originalFile.close()
backupFile.close()

# Delete content original file
originalFile = open("form.txt" , "w")
readOrgFile = originalFile.write("")
originalFile.close()