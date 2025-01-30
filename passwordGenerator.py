import random
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetLower = alphabetUpper.lower()
numbers = "1234567890"
symbols = "!@#$%^&*()_+-?/:[]<>,;~"

all = alphabetUpper + alphabetLower + numbers + symbols

print("Your safe pass is:")
password = "".join(random.sample(all,16))
print(password)