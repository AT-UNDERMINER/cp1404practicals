"""
Damien Turner
CP1404 - Practical Solution
Program description: Taxi simulator program using Taxi and SilverServiceTaxi classes.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the taxi simulator program."""
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("c")
        elif choice == "d":
            print("d")
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").lower()

    print("Thank you for using the taxi simulator.")


def load_taxis():
    """Create and return the list of predefined taxis."""
    return [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]


def display_taxis(taxis):
    """Display all taxis with their index and string details."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
