from  Maneger import Manager


def iftach_algo_simple(my_cards, lucky_card, lost_card, bungee_mode, score):

    say_bungee = False
    throw_card = []
    to_quit = False
    error = ""
    from_stack = True

    luc = lucky_card
    for i, card in enumerate(my_cards):
        if card == luc:
            my_cards[i] = 0

    if lost_card == None:
        if sum(my_cards) <= 5:
            say_bungee = True
            dict = {
            'say_bungee': say_bungee,
            'from_stack': from_stack,
            'quit': to_quit,
            'error': error,
            'throw_cards': throw_card
            }
            return dict

        throw_card = best_cards(my_cards, lost_card, bungee_mode, score)
        dict = {
            'say_bungee': say_bungee,
            'from_stack': from_stack,
            'quit': to_quit,
            'error': error,
            'throw_cards': throw_card
        }
        return dict

    index_best_array = best_cards(my_cards, lost_card, bungee_mode, score)
    is_bungee = if_to_say_bungee(my_cards, lost_card, bungee_mode, score, index_best_array)

    if bungee_mode:
        if not is_bungee:
            to_quit = True
        elif is_bungee:
            say_bungee = True
        if is_bungee == None:
            from_stack = False
            throw_card = index_best_array
    else:
        pass


def best_cards(my_cards, lost_card, bungee_mode, score):
    max_cards = max(my_cards)
    array = []
    for i, card in enumerate(my_cards):
        if card == max_cards:
            array.append(i)
    return array


def where_to_get(my_cards, lost_card, bungee_mode, score, index_best_array):
    t = None
    if lost_card == index_best_array[0]:
        return None
    else:
        for i in my_cards:
            if lost_card == i:
                t = True
        if t:
            return False




def if_to_say_bungee(my_cards, lost_card, bungee_mode, score, index_best_array):
    my_sam = sum(my_cards)
    if my_sam <= 5:
        bungee = True
        if my_sam - sum(index_best_array) + lost_card < my_sam:
            bungee = None
    elif my_sam - sum(index_best_array) + lost_card <= 5:
        bungee = []
    else:
        bungee = False
    return bungee