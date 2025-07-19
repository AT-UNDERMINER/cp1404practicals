"""
Damien Turner
CP1404 - Practical Solution
Program description: Read/write guitar objects from/to a CSV file.
Estimate: 45 mins
Actual: 38 mins
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read existing guitars, display, add new ones, sort, display, then save."""
    guitars = load_guitars(FILENAME)
    print("Current guitars:")
    display_guitars(guitars)

    guitars = add_new_guitars(guitars)
    guitars.sort()

    print("\nAll guitars sorted:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}.")


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


def add_new_guitars(guitars):
    """Prompt user to add guitars; stop when name is blank."""
    print("\nEnter new guitars (leave blank to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(filename, guitars):
    """Write all guitars back to a CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
