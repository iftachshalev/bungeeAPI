import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
    #     self.my_cards = [0, 2, 6, 6, 10]
    #
    #     # init socket (connect)

    # def bungee_disable(self, instance):
    #     if sum(self.my_cards) <= 5:
    #         instance.disabled = False
    #     else:
    #         instance.disabled = True


class Main_kivyApp(App):
    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    Main_kivyApp().run()
