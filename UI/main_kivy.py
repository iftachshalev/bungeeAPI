import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class Button_1(Button):
    def __init__(self, my_cards, **kwargs):
        super(Button_1, self).__init__(**kwargs)


        print("dssssd")
        if sum(my_cards) <= 5:
            self.disabled = False
        else:
            self.disabled = True
    # pass

class Main_kivyApp(App):
    my_cards = [0, 2, 6, 6, 10]

    # def __init__(self, **kwargs):
    #     super(Main_kivyApp, self).__init__(**kwargs)
    #     print("hi")
    #     if sum(self.my_cards)
    #     print(self.lost_btn.text)

    def bungee_disab(self, instance):
        if sum(self.my_cards) <= 5:
            instance.disabled = False
        else:
            instance.disabled = True

    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    Main_kivyApp().run()
