"""
Damien Turner
CP1404 - Practical Solution
Program description: Read/write guitar objects from/to a CSV file.
Estimate: 45 mins
Actual: TODO: Add time actual
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read, sort by year, and display guitars."""
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from CSV and return list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a numbered list of guitars."""
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar}")


if __name__ == "__main__":
    main()
