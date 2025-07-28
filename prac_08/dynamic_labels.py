"""
Damien Turner
CP1404 - Practical Solution
Program description: Dynamic Labels Program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

FRUITS = ['Apples', 'Bananas', 'Strawberries', 'Blueberries', 'Raspberries', 'Mangoes', 'Pineapples', 'Grapes']

class DynamicLabelsApp(App):
    """Main app class to display a list of names as Labels"""

    def __init__(self, **kwargs):
        """Initialise the app and the name list"""
        super().__init__(**kwargs)
        self.names = FRUITS

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label for each name in the list"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
