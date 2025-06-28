"""
Damien Turner
CP1404 - Practical Solution
Program description: TODO: Add description
Estimate: 20 mins
Actual: TODO: Add time actual
"""


class ProgrammingLanguage:

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
