
import secrets
import string

print("Welcome to Password Generator!")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a positive number.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for i in range(length))

    print("Generated Password:", password)
