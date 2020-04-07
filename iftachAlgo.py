import copy


def simple(my_cards, lucky_card, lost_card, bungee_mode):

    say_bungee = False
    throw_card = []
    to_quit = False
    error = ""
    from_stack = True

    luc = lucky_card
    for i, card in enumerate(my_cards):
        if card == luc:
            my_cards[i] = 0

    index_best_array = best_cards(my_cards)

    if lost_card is None:

        if bungee_mode:
            is_bungee = if_to_say_bungee(my_cards, lost_card, index_best_array)
            if not is_bungee:
                to_quit = True
            elif is_bungee:
                say_bungee = True
            elif is_bungee is None:
                from_stack = False
                throw_card = index_best_array
            user = {
                'say_bungee': say_bungee,
                'from_stack': from_stack,
                'quit': to_quit,
                'error': error,
                'throw_cards': throw_card
            }
            return user

        if sum(my_cards) <= 5:
            say_bungee = True

            user = {
                'say_bungee': say_bungee,
                'from_stack': from_stack,
                'quit': to_quit,
                'error': error,
                'throw_cards': throw_card
            }
            return user

        throw_card = best_cards(my_cards)
        user = {
            'say_bungee': say_bungee,
            'from_stack': from_stack,
            'quit': to_quit,
            'error': error,
            'throw_cards': throw_card
        }

        return user

    is_bungee = if_to_say_bungee(my_cards, lost_card, index_best_array)

    if bungee_mode:

        if not is_bungee:
            to_quit = True
        elif is_bungee:
            say_bungee = True
        if is_bungee is None:
            from_stack = False
            throw_card = index_best_array

    else:

        is_bungee = if_to_say_bungee(my_cards, lost_card, index_best_array)
        if is_bungee:
            say_bungee = True
        elif is_bungee is None:
            from_stack = False
            throw_card = index_best_array
        else:

            where = where_to_get(my_cards, lost_card, index_best_array)
            if where is None:
                new = []
                for i in my_cards:
                    if i != my_cards[index_best_array[0]]:
                        new.append(i)
                new_index_best_array = best_cards(new)
                if my_cards[new_index_best_array[0]] < 4:
                    throw_card = index_best_array
                    from_stack = True
                else:

                    throw_card = new_index_best_array
                    from_stack = False
            if not where:
                throw_card = index_best_array
                from_stack = False
            elif where:
                throw_card = index_best_array
                from_stack = True

    user = {
        'say_bungee': say_bungee,
        'from_stack': from_stack,
        'quit': to_quit,
        'error': error,
        'throw_cards': throw_card
    }

    return user


def best_cards(my_cards):
    old_my_cards = copy.copy(my_cards)
    max_cards = max(my_cards)
    array_max = []
    array = []
    for i, card in enumerate(my_cards):
        if card == max_cards:
            array.append(i)
    t = copy.copy(array)

    array_max.append(array)



def where_to_get(my_cards, lost_card, index_best_array):
    t = None
    if lost_card == index_best_array[0]:
        return t
    for i in my_cards:
        if lost_card == i:
            t = True
    if t:
        return False
    if lost_card <= 5:
        return False
    else:
        return True


def if_to_say_bungee(my_cards, lost_card, index_best_array):
    my_sam = sum(my_cards)

    if my_sam <= 5:
        bungee = True
        if lost_card is not None:
            if my_sam - sum(index_best_array) + lost_card < my_sam:
                bungee = None
        return bungee
    elif lost_card is not None:
        if my_sam - sum(index_best_array) + lost_card <= 5:
            bungee = None
            return bungee

    else:
        bungee = False
        return bungee


name = simple([10, 2, 3, 2, 0], 10, None, False)
print(name)
