"""
Damien Turner
CP1404 - Practical Solution
Program description: Guitar inventory program.
Estimate: 15 mins
Actual: 26 mins
"""

from prac_06.guitar import Guitar


def main():
    """Get guitar data from user and display formatted output."""
    print("My guitars!")
    guitars = []

    # Input loop
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")

    # Output guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
