def algo_simple(my_cards, lucky_card, lost_card, bungee_mode, score):
    last_ind = len(my_cards)-1

    from_stack = True
    say_bungee = False
    throw_card = [last_ind]

    if score <= 5:
        say_bungee = True

    for i, card in enumerate(my_cards):
        if card == lost_card:
            from_stack = False
            if throw_card[0] == i:
                throw_card[0] -= 1

    if len(my_cards) > 2 and my_cards[-1] == my_cards[-2]:
        throw_card = [throw_card[0]-1, throw_card[0]]

    dict = {
        'say_bungee': say_bungee,
        'from_stack': from_stack,
        'quit': False,
        'error': '',
        'throw_cards': throw_card
    }
    print(f"throw: {dict['throw_cards']}, stack: {dict['from_stack']}")
    return dict