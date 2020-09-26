from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from copy import copy
from time import sleep
from Maneger import Play


class MyFloatLayout(Widget):
    btn_card_1 = ObjectProperty(None)
    btn_card_2 = ObjectProperty(None)
    btn_card_3 = ObjectProperty(None)
    btn_card_4 = ObjectProperty(None)
    btn_card_5 = ObjectProperty(None)

    btn_lost = ObjectProperty(None)
    btn_stack = ObjectProperty(None)
    btn_bungee = ObjectProperty(None)

    lbl_lucky_card = ObjectProperty(None)
    lbl_last_player = ObjectProperty(None)
    lbl_num_player = ObjectProperty(None)
    lost_card = None
    HOST = "127.0.0.1"
    PORT = 65432

    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        self.play = Play(2)
        obj = self.play.get_state()
        self.update_state(obj)
        self.my_cards = [0, 3, 3, 6, 10]
        self.num_player = 2
        self.throw_array = []
        self.array_cards = [self.btn_card_1, self.btn_card_2, self.btn_card_3, self.btn_card_4,
                            self.btn_card_5]
        self.lucky_card = 5
        self.last_player = [2, "T"]
        self.update_cards()

    def update_state(self, obj):
        pass

    def update_cards(self):
        self.throw_array = []
        for i in range(5):
            try:
                self.array_cards[i].text = str(self.my_cards[i])
            except IndexError:
                self.array_cards[i].disablde = True
        self.bungee_disabled()
        self.disabled_empty_btn()
        self.update_lost_card()
        self.update_last_player()
        self.update_num_player()
        self.update_lucky_card()

    def bungee_disabled(self):
        if sum(self.my_cards) >= 6:
            self.btn_bungee.disabled = True

    def click_btn_card(self, instans):
        if instans.state == "down":
            self.throw_array.append(instans)
            self.btn_bungee.disabled = True

            self.btn_lost.disabled = False
            if not self.last_player[0]:
                self.btn_lost.disabled = True
            self.btn_stack.disabled = False
            for btn_cards in self.array_cards:
                if btn_cards.text != instans.text:
                    btn_cards.disabled = True

        elif instans.state != "down":
            if len(self.throw_array) == 1:
                del(self.throw_array[0])
            else:
                for i in range(len(self.throw_array) - 1):
                    if instans.id == self.throw_array[i].id:
                        del(self.throw_array[i])

        sac = True
        for i in self.array_cards:
            if i.state == "down":
                sac = False

        if sac:
            self.btn_bungee.disabled = False
            self.btn_lost.disabled = True
            self.btn_stack.disabled = True
            for btn_cards in self.array_cards:
                btn_cards.disabled = False

        self.bungee_disabled()

    def disabled_empty_btn(self):
        for i in self.array_cards:
            if i.text == "":
                i.disabled = True

    def update_lucky_card(self):
        self.lbl_lucky_card.text = "Lucky card - " + str(self.lucky_card)

    def return_turn(self, instans):

        array = []
        t = 0
        for i, card in enumerate(self.my_cards):
            if t == len(self.throw_array):
                break
            if str(card) == self.throw_array[0].text:
                array.append(card)
                t += 1
        if instans.text[0] == "l":
            from_stack = "F"

        else:
            from_stack = "T"
        choice = ""
        old_my_cards = copy(self.my_cards)
        for i in range(len(array)):
            for j in range(len(old_my_cards)):
                if array[i] == old_my_cards[j]:
                    choice += str(j)
                    old_my_cards[j] = 'False'
                    break
        choice += from_stack
        print(choice)

    def update_lost_card(self):
        if not self.last_player[0]:
            self.btn_lost.text = "lost: #"
            self.btn_lost.disabled = True
        else:
            # self.btn_lost.disabled = False
            self.btn_lost.text = "lost: " + str(self.last_player[0])

    def update_last_player(self):
        if self.last_player[-1] == "T":
            where = "Stack"
            self.lbl_last_player.text = "last player throw: " + str(self.last_player[0]) + " and get from the " + where

        elif not self.last_player[0]:
            self.lbl_last_player.text = "You Are The First Player!"

        else:
            where = "Lost"
            self.lbl_last_player.text = "last player throw: " + str(self.last_player[0]) + " and get from the " + where

    def update_num_player(self):
        self.lbl_num_player.text = "player number " + str(self.num_player) + ":"


class MainKivyApp(App):

    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    MainKivyApp().run()
