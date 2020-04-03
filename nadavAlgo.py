
def arr2str(arr):
    return ''.join(str(arr).strip('[]').split(', '))


def algo_simple(my_cards, lucky_card, lost_card, bungee_mode, score):
    last_ind = len(my_cards)-1

    from_stack = True
    say_bungee = False
    throw_card = last_ind

    if score <= 5:
        say_bungee = True

    for i, card in enumerate(my_cards):
        if card == lost_card:
            from_stack = False
            if throw_card == i:
                throw_card -= 1

    if len(my_cards) > 2 and my_cards[-1] == my_cards[-2]:
        throw_card = [throw_card-1, throw_card]

    dict = {
        'say_bungee': say_bungee,
        'from_stack': from_stack,
        'throw_cards': throw_card
    }

    return dict


print(algo_simple([2, 3, 5, 7, 8], 9, 8, False, 25))
print(algo_simple([2, 3, 5, 8, 8], 9, 7, False, 26))
