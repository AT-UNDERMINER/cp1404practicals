"""
Damien Turner
CP1404 - Practical Solution
Program description: GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKilometres(App):
    """Main Program - convert miles to kilometres"""

    def build(self):
        """Build the app"""
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKilometres().run()
