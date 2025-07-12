"""
Damien Turner
CP1404 - Practical Solution
Program description: Guitar class for CP1404 Intermediate Exercise.
Estimate: 20 mins
Actual: 28 mins
"""

CURRENT_YEAR = 2022  # Constant for consistency in age calculations
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, else False."""
        return self.get_age() >= VINTAGE_AGE
