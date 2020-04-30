import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class MyFloatLayout(Widget):
    btn_card_1 = ObjectProperty(None)
    btn_card_2 = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        self.my_card = [1, 2, 3, 4, 6]
        self.update_cards()

    def update_cards(self):
        self.btn_card_1.text = str(self.my_card[0])
        self.btn_card_2.text = str(self.my_card[1])

class Main_kivyApp(App):
    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    Main_kivyApp().run()
