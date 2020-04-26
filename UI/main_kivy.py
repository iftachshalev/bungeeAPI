import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class Main_kivyApp(App):
    my_cards = [0, 2, 6, 6, 10]
    id_buttons = ObjectProperty([])
    print(id_buttons)

    def bungee_disab(self, instance):
        if sum(self.my_cards) <= 5:
            instance.disabled = False
        else:
            instance.disabled = True

    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    Main_kivyApp().run()
