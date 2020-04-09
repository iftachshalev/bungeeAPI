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


class Pairs:

    def __init__(self, pairs=None):
        if pairs is None:
            pairs = []
        self.pairs = pairs

    def set_cards(self, my_cards, lucky_card):
        self.pairs = []
        unique_cards = set(my_cards)
        for card in unique_cards:
            inds = find_in_hand(my_cards, card)
            c = Card(card, inds, lucky_card)
            self.pairs.append(c)
        self.pairs.sort(key=lambda x: x.points)

    def get_points(self):
        score = 0
        for p in self.pairs:
            score += p.points
        return score

    def get_pairs_except_inds(self, inds):
        new_pairs = []
        for i, c in enumerate(self.pairs):
            if c.inds != inds:
                new_pairs.append(c)
        return Pairs(new_pairs)

def main_algo(my_cards, lucky_card, last_card, bungee_mode, score):
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

    if last_card is None:
        last_card = 777

    # say bungee
    if score <= bungee_score:
        say_bungee = True

    # take useful card
    if last_card <= max_use_take:
        from_stack = False

    pairs = Pairs()
    pairs.set_cards(my_cards, lucky_card)

    # find index of card equal to last_card
    last_ind = find_in_hand(my_cards, last_card)
    # get all pairs except it
    rest_pairs = pairs.get_pairs_except_inds(last_ind)
    # take from lost iff
    #   1: last_card is not None (first turn)
    #   2: not in bungee mode
    #   3: have in hand,
    #   4: large enough for dup turn,
    #   5: points of other throw is good enough
    if last_card:
        if not bungee_mode and \
                last_card >= min_dup_take and \
                last_ind and \
                last_card > min_dup_take and \
                rest_pairs.pairs[-1].points > max_use_take:
            from_stack = False

    # find best cards throw
    if from_stack:
        throw_cards = pairs.pairs[-1].inds
    else:
        throw_cards = rest_pairs.pairs[-1].inds

    dict = {
        'say_bungee': say_bungee,
        'from_stack': from_stack,
        'quit': False,
        'error': '',
        'throw_cards': throw_cards
    }
    print(f"throw: {dict['throw_cards']}, stack: {dict['from_stack']}, bungee: {dict['say_bungee']}")
    return dict

def get_pairs_except_inds(pairs, inds):
    new_pairs = []
    for i, c in enumerate(pairs):
        if c.inds != inds:
            new_pairs.append(c)
    return new_pairs

def find_in_hand(cards, card):
    inds = []
    for i, c in enumerate(cards):
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


d = main_algo([2, 1, 5, 5, 7], 5, 7, False, 14)
