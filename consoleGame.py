from Maneger import Play


def game(num):
    play = Play(num)
    while True:
        if play.check_if_end():
            min_player_index, min_score, players_score = play.do_end()
            print(f"Player {min_player_index + 1} is the winner!! His score - {min_score}!! All the players' score - {players_score}")
            play.do_break()
        state = play.get_state()
        print(f'Player number {state["turn"] + 1}\n  Bungee mode - {state["bungeeMode"]}\n  Your score - {state["score"]}'
              f'\n  Your cards - {state["cards"]}  Lucky card - {state["luckyCard"]}  Lost card - {state["lostCard"]}'
              f'\n  The optionals - B[Bungee] Q[quit] [turn]')
        choice = input("  Enter your chose: ")
        if choice == "":
            print("invalid!!!!")
        is_stick = play.do_game(choice)
        state = play.get_state(1)
        if is_stick:
            print("  Wel Done!! You Stick!!")
        elif is_stick is False:
            print("  Oho No!! You Cant Stick!!")
        print(f'  Your score - {state["score"]}'
              f'\n  Your cards - {state["cards"]}  Lost card - {state["lostCard"]}\n======================================\n')


game(3)
