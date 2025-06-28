"""
Damien Turner
CP1404 - Practical Solution
Program description: ProgrammingLanguage class for CP1404 Intermediate Exercise.
Estimate: 20 mins
Actual: 15 mins
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Construct the ProgrammingLanguage values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if a programming language is dynamic"""
        return self.typing == "Dynamic"
