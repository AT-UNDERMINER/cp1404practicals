"""
Damien Turner
CP1404 - Practical Solution
Program description: Taxi simulator program using Taxi and SilverServiceTaxi classes.
"""

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

if __name__ == "__main__":
    main()