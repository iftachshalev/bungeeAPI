import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class My_3App(App):

    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    My_3App().run()