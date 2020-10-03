<<<<<<< HEAD:Game/Maneger.py
from enum import Enum
from Game.Bunjy_Game import Game
from Game.Player import Player
from Game.IO_Class import Input
import random
import copy
from Game import IO_Class
from Algo import iftachAlgo, nadavAlgo, sampleAlgo
from time import sleep
=======
from Bunjy_Game import Game
from Player import Player
import random
import copy
>>>>>>> GameAPIGUI:Maneger.py


class Play:

    def __init__(self, num_of_players):

        """
        :param num_of_players: how mach players play in this game
        set the variables to the game
        """

<<<<<<< HEAD:Game/Maneger.py
class Manager:
    USE_INTERNET = False
    OUTPUT_TO_FILE = False
    OUTPUT_TO_SCREEN = True
    LOG_FILE = 'log.txt'
    HOW_WOCH = False

    def __init__(self, conn=None, array_param=None):
        self.num_user = -1
=======
        self.num_user = num_of_players
>>>>>>> GameAPIGUI:Maneger.py
        self.turn = -1
        self.lucky_card = -1
        self.game = []
        self.player = []
<<<<<<< HEAD:Game/Maneger.py
        self.break_ = 0
        self.array_param = array_param
        self.who_say_bungee = 0
        self.only_robot = None
        self.players_score = False

        self.func_dict = {
            0: None,
            1: sampleAlgo.algo_simple,
            2: iftachAlgo.simple,
            3: nadavAlgo.main_algo
        }

        self.conn = conn

    # prepare game: create users
    def do_start(self):

        self.only_robot = True
        for i in self.array_param:
            if i == 0:
                self.only_robot = False

        self.break_ = 0

        if not self.conn:
            self.USE_INTERNET = False

        # set output obj
        self.out = IO_Class.IO_Class(self.OUTPUT_TO_FILE, self.OUTPUT_TO_SCREEN, self.LOG_FILE, self.conn)

        # user input obj
        self.inp = Input(self.conn, self.func_dict)

        self.num_user = len(self.array_param)
=======
        self.who_say_bungee = 0
        self.sam = 0
        self.break_ = 0
>>>>>>> GameAPIGUI:Maneger.py
        self.game = Game()
        self.is_finish = None

        # init players
        for i in range(self.num_user):
<<<<<<< HEAD:Game/Maneger.py
            self.player.append(Player(self.game, self.out.print, self.func_dict[self.array_param[i]], self.conn))
=======
            self.player.append(Player(self.game))
>>>>>>> GameAPIGUI:Maneger.py

        # choose random turn
        self.turn = random.randrange(len(self.player))

        self.lucky_card = self.game.get_lucky_card()
<<<<<<< HEAD:Game/Maneger.py

        # message number 1

        self.players_score = None

        return Stat.GAME

    # run game: one turn each
    def do_game(self):
        # message number 3
        if self.func_dict[self.array_param[self.turn]] is None:
            self.out.print('------------------------------')
            self.out.print('Player Number: {}'.format(self.turn + 1))
            if self.player[self.turn].bungee_mode:
                self.out.print(" It is Bungee mode NOW!!!!")
            self.out.print(repr(self.player[self.turn]))

        if self.func_dict[self.array_param[self.turn]] is not None and not self.only_robot or self.HOW_WOCH:

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
        if self.func_dict[self.array_param[self.turn]] is not None and not self.only_robot and self.HOW_WOCH:
            self.out.print(" The Robot finished!")
        # message number 2
        return Stat.GAME
=======

    # run game: one turn each
    def do_game(self, user_chose):

        """
        :param user_chose: what the player chose to play(string)(index of the card, if to take a card from the stack or from the lost
            | bungee | quit).
            examples: "4T"(normal), "23F"(normal), "B"(to say bungee), "Q"(to quit).
        :return: is_stick: if the player sticked(False - try and fell, None - didn't try, True - try and success)
        """

        # set if the player sticked to None (means didn't try)
        is_stick = None

        # set object of user_chose
        chose_obj = {
            "bungee": False,
            "quit": False,
            "throwCards": [],
            "fromStack": None
        }
        if user_chose == "B":
            chose_obj["bungee"] = True
        elif user_chose == "Q":
            chose_obj["quit"] = True
        else:
            if user_chose[-1] == "F":
                chose_obj["fromStack"] = False
            elif user_chose[-1] == "T":
                chose_obj["fromStack"] = True
            to_throw = list(user_chose[:-1])
            to_throw = [int(i) for i in to_throw]
            chose_obj["throwCards"] = to_throw

        # check if the player want to quit and if true - call break function
        if chose_obj["quit"]:
            self.do_break()

        # check if the player said bungee and if true - call bungee function
        elif chose_obj["bungee"]:
            self.do_bungee()

        # check if the player do a normal playing and if true - call turn function
        elif chose_obj["throwCards"]:

            # copy cards for change later
            old_my_cards = copy.copy(self.player[self.turn].my_cards)

            # play turn
            self.sam, is_stick = self.player[self.turn].turn(chose_obj["throwCards"], chose_obj["fromStack"])

            # sort my_cards
            self.player[self.turn].sort_array()

            # skip turn if 6
            self.sam = self.sam + 1
            for i in chose_obj["throwCards"]:
                if old_my_cards[i] == 6:
                    self.sam += 1
            self.turn = (self.turn + self.sam) % self.num_user

        return is_stick
>>>>>>> GameAPIGUI:Maneger.py

    # run when player in bungee mode
    def do_bungee(self):

        """
        return: nothing
        do: if it's never done so: change the bungee mode of the  players to true, set is_finish to the turn.
            and plus 1 to the turn
        """

        if not self.is_finish and self.is_finish != 0:
            for i in self.player:
                i.bungee_mode = True
            self.is_finish = self.turn
        self.turn = (self.turn + 1) % self.num_user

    # run when player ask to quit game
    def do_break(self):
<<<<<<< HEAD:Game/Maneger.py
        shore = "Y"  # input("are you shore?[Y / N]:")
        if shore == "Y":
            self.out.print("The game break")
            if self.USE_INTERNET:
                self.out.print("Q")
                self.conn.close()
                self.conn.close()
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
        numin = 0
        minscore = self.players_score[self.turn]
        minplayer_index = self.turn
=======
        """
        :return: nothing
        do: break the game
        """

        exit()

    # on game end: find the winner
    def do_end(self):

        """
        :return: min_player_index, min_score, players_score: min_player_index - the winner's
            index, min_score - the winner's score,  players_score - scores list
        """

        # get array of scores
        players_score = [i.my__score() for i in self.player]

        # get the score of the player that said bungee first
        min_score = players_score[self.turn]

        # set the var min_player_index to the index of the player that said bungee first
        min_player_index = self.turn

        # set tur to turn plus 1
>>>>>>> GameAPIGUI:Maneger.py
        tur = (self.turn + 1) % self.num_user

        # find the player with the smallest score
        while tur != self.turn:
            if players_score[tur] <= min_score:
                min_score = players_score[tur]
                min_player_index = tur
            tur = (tur + 1) % self.num_user
<<<<<<< HEAD:Game/Maneger.py
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
                    self.out.print("Q")
                    self.conn.close()
                return {
                    "winner": e,
                    "score": self.players_score
                }
=======
>>>>>>> GameAPIGUI:Maneger.py

        return min_player_index, min_score, players_score

    def check_if_end(self):

        """
        :return: True/False: True - if the game comes to an and
        """

        if self.is_finish == self.turn:
            return True
        else:
            return False

    def get_state(self, back=0):

        """
        :param back: can be 0 or 1. call with 0 before the game does, and 1 after.
        :return: the state of the specific player. type Object
        """

        if not back:
            obj = self.player[self.turn].__repr__()
        else:
            obj = self.player[(self.turn - self.sam) % self.num_user].__repr__()
        obj["turn"] = self.turn
        return obj

    def get_turn(self):
        """
        :return: the active turn
        """
        return self.turn
