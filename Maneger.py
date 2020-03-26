from enum import Enum
from Bunjy_Game import Game
from Player import Player
import random


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
        self.turn = random.randrange(len(self.player) - 1)
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
            print("invalid text, pleas try againn")
            return Stat.GAME
        what_to_do = what_to_do[0:-1]
        array_num = [int(i) for i in what_to_do]
        success = self.player[self.turn].turn(array_num, is_from_stack)
        if not success:
            return Stat.GAME
        print(self.player[self.turn])
        sam = 1
        for i in array_num:
            if i == 6:
                sam += 1
        self.turn = (self.turn + sam) % self.num_user
        return Stat.GAME

    def do_bungee(self):
        bungee_turn = (self.turn - 1) % self.num_user
        while self.turn != bungee_turn:
            stat = self.do_game()
            if stat == Stat.BREAK:
                return Stat.BREAK
            if stat == Stat.BUNGEE:
                return Stat.GAME
        return Stat.END

    def do_break(self):
        shore = input("are you shore?[Y / N]:")
        if shore == "Y":
            print("The game break")
            return True
        else:
            print("The game continue")
            return Stat.GAME

    def do_end(self):
        print(self.player[self.turn], "wine!!!!!!!!!!!!!!!!")
        return # בלה בלה בלה בלה

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
        if st:
            break
    elif st == Stat.END:
        st = meneger.do_end()