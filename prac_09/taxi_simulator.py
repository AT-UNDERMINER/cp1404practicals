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
    taxis = load_taxis()
    current_taxi = None

    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
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


def choose_taxi(taxis):
    """Let the user choose a taxi from the list."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


if __name__ == "__main__":
    main()
