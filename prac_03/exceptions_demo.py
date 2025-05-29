"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # While loop for non zero denominator check
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1
"""A ValueError will occur if the user enters something that is not an integer."""

# Q2
"""A ZeroDivisionError will occur if the user enters a zero as the denominator."""

# Q3
"""One way that would work is nesting the denominator input in a while loop.
This will keep asking the user for aa denominator input until its non zero."""
