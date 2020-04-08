global nt


class Card:
    P10 = 4

    def __init__(self, card, inds, lucky):
        self.card = card
        self.inds = inds
        self.points = len(inds) * card
        if card == lucky:
            self.points = 0
        elif card == 10:
            self.points = len(inds) * self.P10

    def __repr__(self):
        return f'card: {self.card}, ind: {self.inds}, points: {self.points}\n'


def main_algo(my_cards, lucky_card, lost_card, bungee_mode, score):
    # set nt for count game rounds
    global nt
    try:
        nt += 1
    except NameError:
        nt = 1
    from_stack = True
    say_bungee = False

    # set difference of game states
    if nt <= 3:
        bungee_score = 5
        min_dup_take = 3
        max_use_take = 2
    elif nt <= 6:
        bungee_score = 3
        min_dup_take = 1
        max_use_take = 1
    else:
        bungee_score = 2
        min_dup_take = 0
        max_use_take = 0

    if lost_card is None:
        lost_card = 777

    # say bungee
    if score <= bungee_score:
        say_bungee = True

    # take useful card
    if lost_card <= max_use_take:
        from_stack = False

    # take from lost iff
    #   1: have in hand,
    #   2: large enough for dup turn,
    #   3: not in bungee mode
    if not bungee_mode and \
            find_in_hand(my_cards, lost_card) != [] and \
            lost_card >= min_dup_take:
        from_stack = False

    # find best cards throw
    pairs = get_pairs(my_cards, lucky_card)
    throw_cards = pairs[-1].inds

    dict = {
        'say_bungee': say_bungee,
        'from_stack': from_stack,
        'quit': False,
        'error': '',
        'throw_cards': throw_cards
    }
    # print(f"throw: {dict['throw_cards']}, stack: {dict['from_stack']}")
    return dict

def find_in_hand(my_cards, card):
    inds = []
    for i, c in enumerate(my_cards):
        if c == card:
            inds.append(i)

    return inds

def get_pairs(my_cards, lucky_card):
    pairs = []
    uniqe_cards = set(my_cards)
    for card in uniqe_cards:
        inds = find_in_hand(my_cards, card)
        c = Card(card, inds, lucky_card)
        pairs.append(c)
    pairs.sort(key=lambda x: x.points)
    return pairs


# d = main_algo([2, 4, 5, 5, 7], 5, 1, False, 4)
#
# print(d['throw_cards'])
# print(d['from_stack'])
# print(d['say_bungee'])