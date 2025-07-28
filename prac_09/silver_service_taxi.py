"""
Damien Turner
CP1404 - Practical Solution
Program description: SilverServiceTaxi class, derived from Taxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A specialized Taxi that includes fanciness and flagfall charges."""
    flagfall = 4.50  # Flat charge per fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Adjust the price_per_km using the class variable as a base
        self.price_per_km = Taxi.price_per_km * fanciness
