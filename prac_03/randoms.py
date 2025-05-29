import random

# Q1
# print(random.randint(5, 20))  # line 1
"""It was producing integer values. The smallest value that could be seen is 5 and the largest is 20. """

# Q2
# print(random.randrange(3, 10, 2))  # line 2
"""It was producing integer values with missing numbers.
The smallest value that could be seen is 3 and the largest is 9.
This is due to the 2 step size so the available random numbers are 3, 5, 7, 9.
Therefore, we could not see a 4."""

# Q3
# print(random.uniform(2.5, 5.5))  # line 3
"""It was producing floating point numbers. 
The smallest value that could be seen is 2.5 and the largest is 5.5."""

print(random.randint(1,100))