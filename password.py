import random
import string

length = int(input("Enter desired password length: "))

print("Choose password complexity:")
print("1. Only Letters")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = int(input("Enter choice (1/2/3): "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

if choice == 1:
    characters = letters
elif choice == 2:
    characters = letters + digits
elif choice == 3:
    characters = letters + digits + symbols
else:
    print("Invalid choice!")
    exit()

password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)