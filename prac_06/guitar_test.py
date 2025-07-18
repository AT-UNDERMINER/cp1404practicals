"""
Damien Turner
CP1404 - Practical Solution
Program description: Tests for the Guitar class.
Estimate: 15 mins
Actual: 15 mins
"""

from prac_06.guitar import Guitar


def run_tests():
    """Test the Guitar class methods."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)

    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


if __name__ == "__main__":
    run_tests()
