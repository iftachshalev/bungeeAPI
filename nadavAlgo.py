
# def arr2str(arr):
#     return ''.join(str(arr).strip('[]').split(', '))
#
# def main_algo(my_cards, lucky_card, lost_card, bungee_mode, score):
#     from_stack = True
#     dup_ind = -1
#
#     for i, card in enumerate(my_cards):
#         if card == lost_card:
#             from_stack = False
#             dup_ind = i
#
# def find_in_hand(my_cards, card):
#     for i, c in enumerate(my_cards):
#         if c == card:
#             return i
#     return -1
#
# def get_pairs(my_cards, lucky_card):
#     # sort(my_cards)
#     ind = 0
#     card_arr = []
#     curr_card = my_cards[0]
#     start_ind = 0
#     while ind < len(my_cards)-1:
#         if my_cards[ind+1] != curr_card:
#         else:
#             crd = {
#                 'val': my_cards[ind],
#                 'num': ind-start_ind+1,
#                 'cost': (ind-start_ind+1) * my_cards[ind]
#             }
#
#         ind += 1
#
#     # for i, c in enumerate(my_cards):
#         # if c == card:
#         #     return i
#     return -1

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

    return dict


# print(algo_simple([2, 3, 5, 7, 8], 9, 8, False, 25))
# print(algo_simple([2, 3, 5, 8, 8], 9, 7, False, 26))
