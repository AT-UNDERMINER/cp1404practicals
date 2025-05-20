MIN_LENGTH = 4

password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long.")
    password = input("Enter a password: ")

print('*' * len(password))