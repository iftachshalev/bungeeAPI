import copy


def simple(my_cards, lucky_card, lost_card=None, bungee_mode=False):

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

        throw_card = index_best_array

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

    # old_my_cards = copy.copy(my_cards)
    # array_max = []
    #
    # while len(my_cards) != 0:
    #     max_cards = max(my_cards)
    #     array = []
    #     for i, card in enumerate(my_cards):
    #         if card == max_cards:
    #             array.append(i)
    #     t = copy.copy(array)
    #     for j in t:
    #         del(my_cards[j])
    #     array_max.append(t)
    # array_num = []
    #
    # for i in array_max:
    #     for j in array_max[i]:
    #         r = old_my_cards[i[j]]
    #         array_num.append(r)
    #
    # sam = []
    # sam_index = []
    # for i, card in enumerate(array_num):
    #     b = sum(old_my_cards[array_num[i]])
    #     sam.append(b)
    #     sam_index.append(i)
    # while True:
    #     ril = max(sam)
    #     nux = max(old_my_cards)
    #     a = []
    #     b = []
    #     for i, card in enumerate(old_my_cards):
    #         if i == nux:
    #             a.append(card)
    #             b.append(i)
    #     if sum(a) == ril:
    #         return b
    #     else:
    #         for i in range(len(a)):
    #             del(old_my_cards[b[i]])

    my_old_cards = copy.copy(my_cards)
    old_my_cards = copy.copy(my_cards)

    array_in_array = array_to_best_cards(old_my_cards)
    sum_in_array = array_in_array_to_sum_in_array(array_in_array)
    array_for_return = sum_in_array_to_max_for_return(sum_in_array, array_in_array, my_old_cards)

    return array_for_return


def array_to_best_cards(my_cards):

    array_for_return = []

    while len(my_cards) != 0:
        array_for_delete = []
        max_my_cards = max(my_cards)
        array_in = []

        for i, card in enumerate(my_cards):
            if card == max_my_cards:
                array_in.append(card)
                array_for_delete.append(i)
        array_for_return.append(array_in)
        for i in range(len(array_for_delete)):

            if i == 0:
                del(my_cards[array_for_delete[0]])
            else:
                del (my_cards[array_for_delete[i - 1]])
    return array_for_return


def array_in_array_to_sum_in_array(array_in_array):

    array_for_return = []

    for i in array_in_array:
        array_for_return.append(sum(i))

    return array_for_return


def sum_in_array_to_max_for_return(sum_in_array, array_in_array, my_cards):

    max_sum_in_array = max(sum_in_array)
    index = [1]

    for i, card in enumerate(sum_in_array):
        if card == max_sum_in_array:
            index = i

    number = array_in_array[index][0]
    array_for_return = []

    for i, card in enumerate(my_cards):
        if card == number:
            array_for_return.append(i)

    return array_for_return


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


name = simple([1, 2, 9, 9, 10], 4)

print(name)
