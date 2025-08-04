"""
Damien Turner
CP1404 - Practical Solution
Program description: UnreliableCar class, derived from Car
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable car that may not always drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on reliability."""
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0  # Car did not drive
