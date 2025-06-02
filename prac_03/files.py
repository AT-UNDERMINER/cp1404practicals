"""
CP1404/CP5632 - Practical
File reading and writing examples using different techniques.
"""

# Q1: Ask for user's name and write it to a file
name = input("Enter your name: ")
name_out_file = open("name.txt", "w")
print(name, file=name_out_file)
name_out_file.close()

# Q2: Read name from file and print greeting
name_in_file = open("name.txt", "r")
file_name = name_in_file.read().strip()
name_in_file.close()
print(f"Hi {file_name}!")

# Q3: Read first two numbers from numbers.txt and add them
with open("numbers.txt", "r") as number_in_file:
    first_number = int(number_in_file.readline())
    second_number = int(number_in_file.readline())
    total = first_number + second_number
    print(total)

# Q4: Read all numbers and calculate total
with open("numbers.txt", "r") as number_in_file:
    total = 0
    for line in number_in_file:
        total += int(line)
    print(total)
