# import
import copy


# it is the main function
def simple(my_cards, lucky_card, lost_card, bungee_mode, score):
    print("iftach")
    # Defaults
    say_bungee = False
    throw_card = []
    to_quit = False
    error = ""
    from_stack = True

    # Turning a lucky card to zero
    luc = lucky_card
    for i, card in enumerate(my_cards):
        if card == luc:
            my_cards[i] = 0

    # sort my cards
    my_cards.sort()

    # To get a list of cards to throw
    index_best_array = best_cards(my_cards)

    if not bungee_mode:

        # Conference if index_best_array[0] = 6,Objective: Take out six of the cards at the beginning of the turn
        if index_best_array[0] == 6:

            # I call the function where_to_get
            where = where_to_get(my_cards, lost_card, index_best_array)

            # Conference if where = False
            if where is False & lost_card != 6:
                from_stack = False

            throw_card = index_best_array

            # it is what the software need to return
            user = {
                'say_bungee': say_bungee,
                'from_stack': from_stack,
                'quit': to_quit,
                'error': error,
                'throw_cards': throw_card
            }

            # the software return 'user'
            return user

    # jump into if lost_card is None
    if lost_card is None:

        # Conference if the other player said Bungee
        if bungee_mode:

            # To get if should say Bungee
            is_bungee = if_to_say_bungee(my_cards, lost_card, index_best_array)

            if is_bungee == False:
                to_quit = True

            elif is_bungee:
                say_bungee = True

            elif is_bungee is None:
                throw_card = index_best_array

            # it is what the software need to return
            user = {
                'say_bungee': say_bungee,
                'from_stack': from_stack,
                'quit': to_quit,
                'error': error,
                'throw_cards': throw_card
            }

            # the software return 'user'
            return user

        # Conference if sum of the cards small or worth from five
        if sum(my_cards) <= 5:
            say_bungee = True

            # it is what the software need to return
            user = {
                'say_bungee': say_bungee,
                'from_stack': from_stack,
                'quit': to_quit,
                'error': error,
                'throw_cards': throw_card
            }

            # the software return 'user'
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

        if is_bungee is False:
            to_quit = True
        elif is_bungee:
            say_bungee = True
        if is_bungee is None:
            from_stack = False
            throw_card = index_best_array

    else:

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

    array = []

    for i, card in enumerate(my_cards):
        if card == 6:
            array.append(i)

    if len(array) > 0:
        if len(array) == 1 or len(array) == 3:
            return array

        else:
            return [array[0]]

    else:
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
        rili = True
        array = []

        for i in my_cards:
            number_1 = my_cards[0]
            if i == number_1:
                array.append(0)

        if len(my_cards) == len(array):
            del(my_cards)
            my_cards = []
            rili = False

        if rili:

            for i in range(len(array_for_delete)):
                del(my_cards[i - i])

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

    # new_my_cards = []
    # array = []
    #
    # for i in my_cards:
    #     if i != 6:
    #         new_my_cards.append(i)
    #
    #     else:
    #         array.append(0)
    #
    # who_mach = 0
    #
    # for i in range(len(array)):
    #     who_mach += 3
    #
    # print(who_mach)
    my_sam = sum(my_cards)# + who_mach

    new_best_array = []
    for i in index_best_array:
        new_best_array.append(my_cards[i])

    sam_new_best_array = sum(new_best_array)

    if my_sam <= 5:
        bungee = True

    if lost_card is not None and my_sam - sam_new_best_array + lost_card < my_sam:
            bungee = None

    if lost_card is not None and my_sam - sam_new_best_array + lost_card <= 5:
            bungee = None

    elif lost_card is not None and my_sam - sam_new_best_array == 0 and lost_card <= 5:
        bungee = None
        return bungee

    elif my_sam - sam_new_best_array == 0:
        bungee = None

    else:
        bungee = False

    return bungee


# name = simple([0, 4, 4, 7, 9], 1, 2, True, 3)
#
# print(name)
