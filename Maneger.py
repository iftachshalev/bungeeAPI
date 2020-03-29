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

# Class Manager
# Handle functionality of state machine


class Manager:

    def __init__(self):
        self.num_user = -1
        self.turn = -1
        self.lucky_card = -1
        self.game = []
        self.player = []

    # prepare game: create users
    def do_start(self):
        self.num_user = int(input("Choose Number Of Players:"))
        self.game = Game()

        # init players
        for i in range(self.num_user):
            self.player.append(Player(self.game))

        # choose random turn
        self.turn = random.randrange(len(self.player))

        self.lucky_card = self.game.get_lucky_card()
        return Stat.GAME

    # run game: one turn each
    def do_game(self):
        print('------------------------------')
        print('Player Number:', self.turn + 1)
        print(self.player[self.turn])
        what_to_do = input("Action:  B [Bungee]  Q [Quit]\n>>> ")
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
            print("Error: Invalid text, pleas try again")
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

    # run when player in bungee mode
    def do_bungee(self):
        self.hwo_sae_bungee = copy.copy(self.turn)
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

    # run when player ask to quit game
    def do_break(self):
        shore = input("are you shore?[Y / N]:")
        if shore == "Y":
            print("The game break")
            exit()
        else:
            print("The game continue")
            return Stat.GAME

    # on game end: find the winner
    def do_end(self):
        players_score = [i.my__score() for i in self.player]
        minimaly = min(players_score)
        print(minimaly)
        numin = 0
        for i in range(len(players_score)):
            if players_score[i] == minimaly:
                numin += 1
                now = i
            if numin == 1:
                print("Player Number", self.player[now], "Is The Winner!!!!!!!!!!!!!!!!")
                exit()
        bifwinner = self.hwo_sae_bungee

        def up_turn(bifwinner):
            winner = copy.copy(bifwinner)
            for i in range(bifwinner, self.num_user):
                if players_score[winner] == players_score[i + 1]:
                    winner = i + 1
            return winner

        def doun_turn(winner):
            for i in range(self.hwo_sae_bungee):
                if players_score[i] == players_score[winner]:
                    winner = i
            return winner

        if bifwinner != 0 and bifwinner != self.num_user -1:
            winner = up_turn(bifwinner)
            self.ril_winner = doun_turn(winner)
        elif bifwinner == 0:
            self.ril_winner = up_turn(bifwinner)
        elif bifwinner == -1:
            self.ril_winner = doun_turn(bifwinner)
        print("Player Number", self.player[self.ril_winner], "Is The Winner!!!!!!!!!!!!!!!!")
        exit()


manager = Manager()
st = Stat.START


# game state machine
while True:
    if st == Stat.START:
        st = manager.do_start()
    elif st == Stat.GAME:
        st = manager.do_game()
    elif st == Stat.BUNGEE:
        st = manager.do_bungee()
    elif st == Stat.BREAK:
        st = manager.do_break()
    elif st == Stat.END:
        manager.do_end()

