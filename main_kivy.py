from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from copy import copy
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
    lbl_bungee_mode = ObjectProperty(None)
    lbl_num_player = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        self.num_player = None
        self.my_cards = None
        self.lucky_card = None
        self.lost_card = None
        self.bungee_mode = None
        self.play = Play(3)
        self.obj = self.play.get_state()
        self.update_state()
        self.throw_array = []
        self.array_cards = [self.btn_card_1, self.btn_card_2, self.btn_card_3, self.btn_card_4,
                            self.btn_card_5]
        self.update()

    def update_state(self):
        self.num_player = self.obj["turn"] + 1
        self.my_cards = self.obj["cards"]
        self.lucky_card = self.obj["luckyCard"]
        self.lost_card = self.obj["lostCard"]
        self.bungee_mode = self.obj["bungeeMode"]

    def update(self):
        self.throw_array = []
        for i in range(5):
            self.array_cards[i].state = "normal"
            try:
                self.array_cards[i].text = str(self.my_cards[i])
            except:
                self.array_cards[i].text = ""
                self.array_cards[i].disablde = True
        self.bungee_disabled()
        self.disabled_empty_btn()
        self.update_lost_card()
        self.update_num_player()
        self.update_lucky_card()
        self.update_bungee_mode()

    def click_btn_card(self, instans):
        if instans.state == "down":
            self.throw_array.append(instans)
            self.btn_bungee.disabled = True

            self.btn_lost.disabled = False
            if not self.lost_card:
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
                if btn_cards.text != "":
                    btn_cards.disabled = False
                else:
                    btn_cards.disabled = True

        self.bungee_disabled()

    def return_turn(self, instans):
        if instans.text == self.btn_bungee.text:
            choice = "B"
        else:
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
        is_stick = self.play.do_game(choice)
        if is_stick:
            print("  Wel Done!! You Stick!!")
        elif is_stick is False:
            print("  Oho No!! You Cant Stick!!")
        if self.play.check_if_end():
            min_player_index, min_score, players_score = self.play.do_end()
            print(f"Player {min_player_index + 1} is the winner!! His score - {min_score}!! All the players' score - {players_score}")
            self.play.do_break()
        self.obj = self.play.get_state()
        self.update_state()
        self.update()

    def disabled_empty_btn(self):
        for i in self.array_cards:
            if i.text == "":
                i.disabled = True
            else:
                i.disabled = False

    def bungee_disabled(self):
        if self.obj["score"] >= 6:
            self.btn_bungee.disabled = True
        else:
            self.btn_bungee.disabled = False

    def update_lucky_card(self):
        self.lbl_lucky_card.text = "Lucky card - " + str(self.lucky_card)

    def update_lost_card(self):
        if not self.lost_card:
            self.btn_lost.text = "lost: #"
            self.btn_lost.disabled = True
        else:
            self.btn_lost.text = "lost: " + str(self.lost_card)

    def update_num_player(self):
        self.lbl_num_player.text = "player number " + str(self.num_player) + ":"

    def update_bungee_mode(self):
        self.lbl_bungee_mode.text = "Bungee mode - " + str(self.bungee_mode)

class MainKivyApp(App):

    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    MainKivyApp().run()
