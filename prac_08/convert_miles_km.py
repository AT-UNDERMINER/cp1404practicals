"""
Damien Turner
CP1404 - Practical Solution
Program description: GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesToKilometres(App):
    """Main Program - convert miles to kilometres"""

    output_text = StringProperty()

    def build(self):
        """Build the app"""
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = '0.0 km'
        return self.root

    def handle_convert(self):
        """Convert miles to kilometres and update label"""
        input_miles = self.verify_miles_input(self.root.ids.input_miles.text)
        output_kilometers = float(input_miles) * MILES_TO_KM
        self.output_text = f'{output_kilometers} km'

    def handle_increment(self, amount):
        """Increment the miles input up/down by a value"""
        input_miles = self.verify_miles_input(self.root.ids.input_miles.text)
        input_miles += amount
        self.root.ids.input_miles.text = str(input_miles)
        self.handle_convert()

    def verify_miles_input(self, input_miles):
        """Verify the input is a float type"""
        try:
            verified_miles = float(input_miles)
            return verified_miles
        except ValueError:
            return 0


ConvertMilesToKilometres().run()
