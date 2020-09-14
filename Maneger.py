from enum import Enum
from Bunjy_Game import Game
from Player import Player
from IO_Class import Input
import random
import copy
import IO_Class


class Manager:
    OUTPUT_TO_FILE = True
    OUTPUT_TO_SCREEN = True
    LOG_FILE = 'log.txt'

    def __init__(self, num_of_players):
        self.num_user = num_of_players
        self.turn = -1
        self.lucky_card = -1
        self.game = []
        self.player = []
        self.who_say_bungee = 0
        self.break_ = 0
        self.sam = 0
        self.break_ = 0
        # set output obj
        # self.out = IO_Class.IO_Class(self.OUTPUT_TO_FILE, self.OUTPUT_TO_SCREEN, self.LOG_FILE)

        # user input obj
        # self.inp = Input()

        self.game = Game()

        # init players
        for i in range(self.num_user):
            self.player.append(Player(self.game))

        # choose random turn
        self.turn = random.randrange(len(self.player))

        self.lucky_card = self.game.get_lucky_card()

    # run game: one turn each
    def do_game(self, throw_cards, from_stack, to_turn=None):

        if to_turn:
            self.turn = to_turn

        # self.out.print('------------------------------')
        # self.out.print('Player Number: {}'.format(self.turn + 1))
        # if self.player[self.turn].bungee_mode:
        #     self.out.print(" It is Bungee mode NOW!!!!")
        # self.out.print(repr(self.player[self.turn]))

        # get user or robot command
        # my_cards, lucky_card, lost_card, bungee_mode, score = self.player[self.turn].get_state()
        # command_dict = self.inp.get_turn(my_cards, lucky_card, lost_card, bungee_mode, score)

        # copy cards for change later
        old_my_cards = copy.copy(self.player[self.turn].my_cards)

        # array = [self.player[self.turn].my_cards[i] for i in throw_cards]
        # self.out.print(f" throw: {array[:]}, stack: {from_stack}")

        # play turn
        success, self.sam = self.player[self.turn].turn(throw_cards, from_stack)

        # sort my_cards
        self.player[self.turn].sort_array()

        # turn failed
        if not success:
            return False

        # self.out.print(repr(self.player[self.turn]))

        # skip turn if 6
        self.sam = self.sam + 1
        for i in throw_cards:
            if old_my_cards[i] == 6:
                self.sam += 1
        self.turn = (self.turn + self.sam) % self.num_user

        self.break_ += 1

        return True

    # run when player in bungee mode
    def do_bungee(self):
        for i in self.player:
            i.bungee_mode = True
        # bungee_turn = (self.turn - 1) % self.num_user
        # while self.turn != bungee_turn:
        #     stat = self.do_game()
        #     if stat == Stat.BREAK:
        #         return Stat.BREAK
        #     elif stat == Stat.BUNGEE:
        #         pass
        #         # self.turn = (self.turn + 1) % self.num_user
        #     else:
        #         for i in range(self.sam):
        #             tmp_turn = (self.turn - i) % self.num_user
        #             if tmp_turn == bungee_turn:
        #                 self.turn = bungee_turn
        #                 break

        # self.turn = (self.turn + 1) % self.num_user

    # run when player ask to quit game
    def do_break(self):
        exit()

    # on game end: find the winner
    def do_end(self):
        self.players_score = [i.my__score() for i in self.player]
        minimaly = min(self.players_score)
        numin = 0
        minscore = self.players_score[self.turn]
        minplayer_index = self.turn
        tur = (self.turn + 1) % self.num_user
        while tur != self.turn:
            if self.players_score[tur] <= minscore:
                minscore = self.players_score[tur]
                minplayer_index = tur
            tur = (tur + 1) % self.num_user
        return minplayer_index, minscore, self.players_score

    def get_state(self, is_first):
        if is_first:
            return self.player[self.turn].__repr__()
        else:
            return self.player[(self.turn - self.sam) % self.num_user].__repr__()

    def get_some_variables(self):
        return self.turn, self.player[self.turn].bungee_mode

