word = input("Enter the word: ")

vowelCount = 0

for char in word :
    if char.lower() in "aeiou" :
        vowelCount += 1
print(f"The word contains {vowelCount} vowels.")