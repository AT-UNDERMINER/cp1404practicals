"""
Damien Turner
CP1404 - Practical Solution
Program description: Test for SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare calculation."""
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)  # Fanciness of 2

    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()
    print(fancy_taxi)
    print(f"Fare for 18 km = ${fare:.2f}")

    # Check fare is correct: 18 km * (1.23 * 2) + 4.50 = 48.78
    # assert abs(fare - 48.78) < 0.01, f"Expected fare ~48.78, got {fare:.2f}"

    # New assert assuming rounded value to the nearest 10c
    assert fancy_taxi.get_fare() == 48.80  # assert the 18km trip is rounded


if __name__ == "__main__":
    main()
