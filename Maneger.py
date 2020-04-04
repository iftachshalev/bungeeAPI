from enum import Enum
from Bunjy_Game import Game
from Player import Player
from IO_Class import Input
import random
import copy
import IO_Class

class Stat(Enum):
    START = 1
    GAME = 2
    BUNGEE = 3
    BREAK = 4
    END = 5

# Class Manager
# Handle functionality of state machine


class Manager:
    OUTPUT_TO_FILE = True
    OUTPUT_TO_SCREEN = True
    INPUT_FROM_FUNC = False
    LOG_FILE = 'log.txt'

    def __init__(self):
        self.num_user = -1
        self.turn = -1
        self.lucky_card = -1
        self.game = []
        self.player = []

        # set output obj
        self.out = IO_Class.IO_Class(self.OUTPUT_TO_FILE, self.OUTPUT_TO_SCREEN, self.LOG_FILE)

        # user input obj
        self.inp = Input(self.INPUT_FROM_FUNC)

        # set func dictionary

        # Init to Input class
        # save to self.inp

    # prepare game: create users
    def do_start(self):
        self.num_user = int(input("Choose Number Of Players:"))
        self.game = Game()

        # init players
        for i in range(self.num_user):
            self.player.append(Player(self.game, self.out.print))

        # choose random turn
        self.turn = random.randrange(len(self.player))

        self.lucky_card = self.game.get_lucky_card()
        return Stat.GAME

    # run game: one turn each
    def do_game(self):
        self.out.print('------------------------------')
        self.out.print('Player Number: {}'.format(self.turn + 1))
        self.out.print(repr(self.player[self.turn]))

        # get user or robot command
        my_cards, lucky_card, lost_card, bungee_mode, score = self.player[self.turn].get_state()
        command_dict = self.inp.get_turn(self.turn, my_cards, lucky_card, lost_card, bungee_mode, score)

        # spatial cases
        if command_dict['error'] != '':
            self.out.print(command_dict['error'])
            return Stat.GAME
        elif command_dict['quit']:
            return Stat.BREAK
        elif command_dict['say_bungee']:
            self.turn = (self.turn + 1) % self.num_user
            return Stat.BUNGEE

        # copy cards for change later
        old_my_cards = copy.copy(self.player[self.turn].my_cards)

        # play turn
        success, self.sam = self.player[self.turn].turn(command_dict['throw_cards'], command_dict['from_stack'],)

        # turn failed
        if not success:
            return Stat.GAME

        # print state afterwards
        self.out.print(repr(self.player[self.turn]))

        # skip turn if 6
        self.sam = self.sam + 1
        for i in command_dict['throw_cards']:
            if old_my_cards[i] == 6:
                self.sam += 1
        self.turn = (self.turn + self.sam) % self.num_user
        return Stat.GAME

    # run when player in bungee mode
    def do_bungee(self):
        self.who_say_bungee = copy.copy(self.turn)
        for i in self.player:
            i.bungee_mode = True
        bungee_turn = (self.turn - 1) % self.num_user
        while self.turn != bungee_turn:
            stat = self.do_game()
            if stat == Stat.BREAK:
                return Stat.BREAK
            if stat == Stat.BUNGEE:
                self.turn = (self.turn + 1) % self.num_user
        self.turn = (self.turn + 1) % self.num_user
        return Stat.END

    # run when player ask to quit game
    def do_break(self):
        shore = input("are you shore?[Y / N]:")
        if shore == "Y":
            self.out.print("The game break")
            exit()
        else:
            self.out.print("The game continue")
            return Stat.GAME

    # on game end: find the winner
    def do_end(self):
        players_score = [i.my__score() for i in self.player]
        minimaly = min(players_score)
        self.out.print(str(minimaly))
        numin = 0
        minscore = players_score[self.turn]
        tur = (self.turn + 1) % self.num_user
        while tur != self.turn:
            if players_score[tur] <= minscore:
                minscore = players_score[tur]
                minplayer = self.player[tur]
                minplayer_index = tur
            tur = (tur + 1) % self.num_user
        self.out.print("Player Number: {} Is The Winner!!!!!!!!!!!!!!!!".format(minplayer_index + 1))
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