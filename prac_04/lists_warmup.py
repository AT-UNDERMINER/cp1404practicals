"""
Damien Turner
CP1404 - Practical Solution
Program description: lists_warmup.py questions answers
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]  # [3]
numbers[-1]  # [2]
numbers[3]  # [1]
numbers[:-1]  # [3, 1, 4, 1, 5, 9]
numbers[3:4]  # [1]
5 in numbers  # True
7 in numbers  # False
"3" in numbers  # False
numbers + [6, 5, 3]  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#  Q1
numbers[0] = "ten"

# Q2
numbers[-1] = 1

# Q3
print(numbers[2:])

# Q4
print(9 in numbers)
