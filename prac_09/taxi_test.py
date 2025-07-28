"""
Damien Turner
CP1404 - Practical Solution
Program description: Test the Taxi class using drive and fare-related methods.
"""

from taxi import Taxi


def main():
    """Test the Taxi class."""
    # Create a new taxi object
    my_taxi = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi 40 km
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Start a new fare and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
