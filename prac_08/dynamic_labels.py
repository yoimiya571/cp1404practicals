"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create labels based on content of dictionary
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic Label creation."""
    status_text = StringProperty("Dynamic Labels Example")

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name, phone in self.name_to_phone.items():
            # Create a label for each name and phone number
            temp_label = Label(text=f"{name}: {phone}")
            # Add the label to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()