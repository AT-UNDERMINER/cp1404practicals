"""
Damien Turner
CP1404 - Practical Solution
Program description: Band class using aggregation - a Band has Musicians
"""


class Band:
    """Represent a band that contains a list of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of the band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
