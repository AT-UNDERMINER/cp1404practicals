"""
Damien Turner
CP1404 - Practical Solution
Program description: list_exercises.py solutions
"""

# 1)
numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# 2)
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Entre username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

# Extension
numbers = []
number = 0
i = 0

while number >= 0:
    i += 1
    number = int(input(f"Number {i}: "))
    if number >= 0:
        numbers.append(number)

if numbers:
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
else:
    print("No valid numbers were entered.")
