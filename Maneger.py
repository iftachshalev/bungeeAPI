from enum import Enum
from Bunjy_Game import Game
from Player import Player
from IO_Class import Input
import random
import copy
import IO_Class
import nadavAlgo
import sampleAlgo
import iftachAlgo
from time import sleep
import socket


class Stat(Enum):
    START = 1
    GAME = 2
    BUNGEE = 3
    BREAK = 4
    END = 5

# Class Manager
# Handle functionality of state machine


class Manager:
    HOST = '127.0.0.1'
    PORT = 65432
    USE_INTERNET = True
    OUTPUT_TO_FILE = True
    OUTPUT_TO_SCREEN = False
    INPUT_FROM_FUNC = True
    LOG_FILE = 'log.txt'
    ROBOT_NUM_USER = 3

    def __init__(self, array_param=None):

        self.num_user = -1
        self.turn = -1
        self.lucky_card = -1
        self.game = []
        self.player = []
        self.break_ = 0
        self.array_param = array_param
        self.who_say_bungee = 0

        self.func_dict = {
            0: None,
            1: sampleAlgo.algo_simple,
            2: iftachAlgo.simple,
            3: nadavAlgo.main_algo
        }
        if self.USE_INTERNET:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((self.HOST, self.PORT))

            self.s.listen()
            self.conn, addr = self.s.accept()

    # prepare game: create users
    def do_start(self):

        self.break_ = 0

        # set output obj
        self.out = IO_Class.IO_Class(self.OUTPUT_TO_FILE, self.OUTPUT_TO_SCREEN, self.LOG_FILE, self.conn)

        # user input obj
        self.inp = Input(self.conn, self.func_dict)

        self.num_user = len(self.array_param)
        self.game = Game()

        # init players
        for i in range(self.num_user):
            self.player.append(Player(self.game, self.out.print, self.func_dict[self.array_param[i]], self.conn))

        # choose random turn
        self.turn = random.randrange(len(self.player))

        self.lucky_card = self.game.get_lucky_card()
        return Stat.GAME

    # run game: one turn each
    def do_game(self):
        if self.OUTPUT_TO_SCREEN and self.func_dict[self.array_param[self.turn]] is None:
            self.out.print('------------------------------')
            self.out.print('Player Number: {}'.format(self.turn + 1))
            if self.player[self.turn].bungee_mode:
                self.out.print(" It is Bungee mode NOW!!!!")
            self.out.print(repr(self.player[self.turn]))

        if self.func_dict[self.array_param[self.turn]] is not None:

            self.out.print('------------------------------')

            self.out.print(f"It is Robot number {self.turn + 1}")
            sleep(1)
            self.out.print(" The Robot thinking...")
            sleep(1)
            self.out.print(" .")
            sleep(1)
            self.out.print(" .")
            sleep(1)
            self.out.print(" .")
            sleep(1)

        # get user or robot command
        my_cards, lucky_card, lost_card, bungee_mode, score = self.player[self.turn].get_state()
        # command_dict = self.inp.get_turn(self.turn, my_cards, lucky_card, lost_card, bungee_mode, score)
        command_dict = self.player[self.turn].inp.get_turn(my_cards, lucky_card, lost_card, bungee_mode, score)

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

        array = [self.player[self.turn].my_cards[i] for i in command_dict['throw_cards']]
        self.out.print(f" throw: {array}, stack: {command_dict['from_stack']}")

        # play turn
        success, self.sam = self.player[self.turn].turn(command_dict['throw_cards'], command_dict['from_stack'],)

        # sort my_cards
        self.player[self.turn].sort_array()

        # turn failed
        if not success:
            return Stat.GAME

        # print state afterwards2

        if self.OUTPUT_TO_SCREEN and self.func_dict[self.array_param[self.turn]] is None:
            self.out.print(repr(self.player[self.turn]))

        # skip turn if 6
        self.sam = self.sam + 1
        for i in command_dict['throw_cards']:
            if old_my_cards[i] == 6:
                self.sam += 1
        self.turn = (self.turn + self.sam) % self.num_user

        self.break_ += 1

        # cheek if has a bug in the software
        if self.break_ > 200:
            return Stat.BREAK
        if self.func_dict[self.array_param[self.turn]] is not None:
            self.out.print(" The Robot finished!")
        return Stat.GAME

    # run when player in bungee mode
    def do_bungee(self):
        for i in self.player:
            i.bungee_mode = True
        bungee_turn = (self.turn - 1) % self.num_user
        while self.turn != bungee_turn:
            stat = self.do_game()
            if stat == Stat.BREAK:
                return Stat.BREAK
            elif stat == Stat.BUNGEE:
                pass
                # self.turn = (self.turn + 1) % self.num_user
            else:
                for i in range(self.sam):
                    tmp_turn = (self.turn - i) % self.num_user
                    if tmp_turn == bungee_turn:
                        self.turn = bungee_turn
                        break

        # self.turn = (self.turn + 1) % self.num_user
        return Stat.END

    # run when player ask to quit game
    def do_break(self):
        shore = "Y"# input("are you shore?[Y / N]:")
        if shore == "Y":
            self.out.print("The game break")
            if self.USE_INTERNET:
                self.out.print("Q")
                self.conn.close()
                self.s.close()
            else:
                if self.USE_INTERNET:
                    self.conn.close()
                exit()
        else:
            self.out.print("The game continue")
            return Stat.GAME

    # on game end: find the winner
    def do_end(self):
        self.players_score = [i.my__score() for i in self.player]
        minimaly = min(self.players_score)
        self.out.print(str(minimaly))
        numin = 0
        minscore = self.players_score[self.turn]
        minplayer_index = self.turn
        tur = (self.turn + 1) % self.num_user
        while tur != self.turn:
            if self.players_score[tur] <= minscore:
                minscore = self.players_score[tur]
                minplayer_index = tur
            tur = (tur + 1) % self.num_user
        self.out.print("")
        self.out.print("Player Number: {} Is The Winner!!!!!!!!!!!!!!!!".format(minplayer_index + 1))
        self.out.print(f"his score - {minscore}")
        return minplayer_index


    # game state machine
    def run(self):
        st = Stat.START
        while True:
            # time.sleep(1)
            if st == Stat.START:
                st = self.do_start()
            elif st == Stat.GAME:
                st = self.do_game()
            elif st == Stat.BUNGEE:
                st = self.do_bungee()
            elif st == Stat.BREAK:
                st = self.do_break()
            elif st == Stat.END:
                e = self.do_end()
                if self.USE_INTERNET:
                    self.conn.close()
                return {
                    "winner": e,
                    "score": self.players_score
                }


