from enum import Enum
from Bunjy_Game import Game
from Player import Player
import random
import copy


class Stat(Enum):
    START = 1
    GAME = 2
    BUNGEE = 3
    BREAK = 4
    END = 5

class Meneger:

    def do_start(self):
        self.num_user = int(input("num players:"))
        self.game = Game()
        self.player = []
        for i in range(self.num_user):
            self.player.append(Player(self.game))
        self.turn = random.randrange(len(self.player))
        self.lucky_card = self.game.get_lucky_card()
        # self.lost_card = self.game.get_lost_card()
        return Stat.GAME

    def do_game(self):
        print(self.turn + 1)
        print(self.player[self.turn])
        what_to_do = input("what do you want todo?\n   B [To sae Bungee]\n   Q [to quit]")
        if what_to_do == "B":
            self.turn = (self.turn + 1) % self.num_user
            return Stat.BUNGEE
        if what_to_do == "Q":
            return Stat.BREAK
        is_from_stack = what_to_do[-1]
        if is_from_stack == "T":
            is_from_stack = True
        elif is_from_stack == "F":
            is_from_stack = False
        else:
            print("invalid text, pleas try again")
            return Stat.GAME
        old_my_cards = copy.copy(self.player[self.turn].my_cards)
        what_to_do = what_to_do[0:-1]
        array_num = []
        for i in what_to_do:
            card_ind = int(i)
            if card_ind >= len(old_my_cards):
                print('ERROR: card index must be in hand')
                return Stat.GAME
            array_num.append(card_ind)
        success, self.sam = self.player[self.turn].turn(array_num, is_from_stack)
        if not success:
            return Stat.GAME
        print(self.player[self.turn])
        self.sam = self.sam + 1
        for i in array_num:
            if old_my_cards[i] == 6:
                self.sam += 1
        self.turn = (self.turn + self.sam) % self.num_user
        return Stat.GAME

    def do_bungee(self):
        for i in self.player:
            i.bungee_mode = True
        bungee_turn = (self.turn - 1) % self.num_user
        while self.turn != bungee_turn:
            stat = self.do_game()
            if stat == Stat.BREAK:
                return Stat.BREAK
            if stat == Stat.BUNGEE:
                self.turn = (self.turn + 1) % self.num_user
        return Stat.END

    def do_break(self):
        self.hwo_sae_bungee = self.player[self.turn]
        shore = input("are you shore?[Y / N]:")
        if shore == "Y":
            print("The game break")
            exit()
        else:
            print("The game continue")
            return Stat.GAME

    def do_end(self):
        players_score = [i for i in self.player]
        minimaly = min(players_score)
        print(minimaly)
        numin = 0
        for i in range(len(players_score)):
            if players_score[i] == minimaly:
                numin += 1
                now = i
            if numin == 1:
                print(self.player[now], "wine!!!!!!!!!!!!!!!!")
                exit()



meneger = Meneger()
st = Stat.START

while True:
    if st == Stat.START:
        st = meneger.do_start()
    elif st == Stat.GAME:
        st = meneger.do_game()
    elif st == Stat.BUNGEE:
        st = meneger.do_bungee()
    elif st == Stat.BREAK:
        st = meneger.do_break()
    elif st == Stat.END:
        st = meneger.do_end()

