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
    total_bill = 0.0

    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                trip_cost = drive_taxi(current_taxi)
                total_bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
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


def drive_taxi(taxi):
    """Drive the taxi for a given distance and return the cost."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance. Assuming 0 km.")
        return 0.0

    taxi.start_fare()
    taxi.drive(distance)
    return taxi.get_fare()


if __name__ == "__main__":
    main()
