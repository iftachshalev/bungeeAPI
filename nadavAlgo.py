
def algo_simple(my_cards, lucky_card, lost_card, bungee_mode, score):
    last_ind = len(my_cards)-1

    from_stack = 'T'
    throw_card = last_ind

    if score <= 5:
        return 'B'

    for card in my_cards:
        if card == lost_card:
            from_stack = 'F'

    if len(my_cards) > 2 and[-1] == my_cards[-2]:
        throw_card = [last_ind-1, last_ind]

    throw_str = ''.join(str(throw_card).strip('[]').split(', '))
    return throw_str + from_stack