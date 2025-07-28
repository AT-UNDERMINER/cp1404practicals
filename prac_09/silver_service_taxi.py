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

    def __str__(self):
        """Return string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate fare including flagfall."""
        base_fare = super().get_fare()
        return base_fare + self.flagfall
