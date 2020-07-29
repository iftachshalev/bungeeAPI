import random
import copy


class Game:
    cards_type = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6,
                  6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10,
                  0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6,
                  6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10
                  ]

    # it is the init
    def __init__(self):

        # random.shuffle(self.cards)
        self.reset_cards()

        # get lucky card
        self.lucky_card = self.get_valid_lucky_card()

        # reset the lost cards to False
        self.lost_cards = []

    # func to throw cads
    def throw_card(self, *args):
        if len(args) == 1:
            self.lost_cards.append(args[0])
            return
        else:
            for i in args:
                self.lost_cards.append(i)
            return

    # get card from stack
    def card_from_stack(self):
        if len(self.cards) == 0:
            # self.cards = self.lost_cards[:-1]
            # random.shuffle(self.cards)
            # del(self.lost_cards[:-1])
            self.reset_cards()
        card = self.cards[-1]
        del(self.cards[-1])
        return card

    # get card from lost cards
    def card_from_lost(self):
        success = True
        card = self.lost_cards[-1]
        del (self.lost_cards[-1])
        return card, success

    def __repr__(self):
        return f"cards - {self.cards}\n, lucky card - {self.lucky_card}, lost_cards - {self.lost_cards}"

    # get lucky card to the Player Class
    def get_lucky_card(self):
        return self.lucky_card

    # get lost card to the Player Class
    def get_lost_card(self):
        try:
            return self.lost_cards[-1]
        except:
            return None

    # get lucky card that not == to 6 or 0
    def get_valid_lucky_card(self):
        while True:
            card = self.cards[-1]
            if card != 0 and card != 6:
                del(self.cards[-1])
                break
            else:
                del(self.cards[-1])
                self.cards.insert(0, card)
        return card

    # do random to the list cards in the stack
    def reset_cards(self):
        self.cards = copy.copy(self.cards_type)
        random.shuffle(self.cards)

