from Bunjy_Game import Game

class Player:

    # lucky card

    def __init__(self, game):
        self.game = game
        self.my_cards = []
        for i in range(5):
            card = self.game.card_from_stack()
            self.my_cards.append(card)
        self.lucky_card = self.game.get_lucky_card()
        self.sort_array()
        self.lost_card = self.game.get_lost_card()
        self.bungee_mode = False
        self.my_score = self.my__score()
        self.stick_factor = 0.5

    def say_bungee(self):
        if sum(self.my_cards) <= 5:
            self.bungee_mode = True
        else:
            print("ERROR!")

    def turn(self, throw_index, from_stack):
        self.lost_card = self.game.get_lost_card()
        if not from_stack and self.lost_card == None:
            print("ERROR! You cent put card from lost if you play 1")
            return False
        throw_lost = len(throw_index)
        throw_index.sort()
        for j in range(len(throw_index) - 1):
            if self.my_cards[throw_index[j]] != self.my_cards[throw_index[j + 1]]:
                print("ERROR! You cannot throw unequal cards")
                return False
        for i in range(len(throw_index)):
            self.game.throw_card(self.my_cards[throw_index[- (i + 1)]])
            del(self.my_cards[throw_index[-(i + 1)]])
        if from_stack:
            card = self.game.card_from_stack()
        if not from_stack:
            card, success = self.game.card_from_lost(throw_lost)
        if card != []:
            self.my_cards.append(card)
            self.sort_array()
            # to stick
            return True
        return False

    def get_state(self):
        lost_card = self.game.get_lost_card()
        return self.my_cards, self.lucky_card, lost_card, self.bungee_mode

    def my__score(self):
        sam = 0
        for i in self.my_cards:
            if i == self.lucky_card:
                pass
            else:
                sam += i
        return sam

    def __repr__(self):
        lost_card = self.game.get_lost_card()
        return f"my cards - {self.my_cards}, lucky card - {self.lucky_card}, lost_card - {lost_card}," \
            f" bungee_mode - {self.bungee_mode}, my score - {self.my__score()}"

    def get_lucky_card_to_zero(self):
        for i in range(len(self.my_cards)):
            if self.my_cards[i] == self.lucky_card:
                self.my_cards[i] = 0

    def get_my_cards_to_maneger(self):
        return self.my_cards

    def sort_array(self):
        array = []
        for i in range(len(self.my_cards) - 2):
            if self.my_cards[i] == self.lucky_card:
                array.append(self.my_cards[i])
                del(self.my_cards[i])
        self.my_cards.sort()
        for i in self.my_cards:
            array.append(i)
        self.my_cards = array

g = Game()
p = Player(g)
