"""
Damien Turner
CP1404 - Practical Solution
Program description: Test for UnreliableCar class
"""

from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    unreliable_car = UnreliableCar("Maybe", 100, 30.0)

    print("\nUnreliable Car Test:")
    for i in range(10):
        distance = unreliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance} km")


if __name__ == "__main__":
    main()
