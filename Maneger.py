from Bunjy_Game import Game
from Player import Player
import random
import copy


class Play:

    def __init__(self, num_of_players):

        """
        :param num_of_players: how mach players play in this game
        set the variables to the game
        """

        self.num_user = num_of_players
        self.turn = -1
        self.lucky_card = -1
        self.game = []
        self.player = []
        self.who_say_bungee = 0
        self.sam = 0
        self.break_ = 0
        self.game = Game()
        self.is_finish = None

        # init players
        for i in range(self.num_user):
            self.player.append(Player(self.game))

        # choose random turn
        self.turn = random.randrange(len(self.player))

        self.lucky_card = self.game.get_lucky_card()

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
        tur = (self.turn + 1) % self.num_user

        # find the player with the smallest score
        while tur != self.turn:
            if players_score[tur] <= min_score:
                min_score = players_score[tur]
                min_player_index = tur
            tur = (tur + 1) % self.num_user

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
