from Maneger import Manager


def game(num):
    gameModule = Manager(num)
    to_exit = False
    global_turn = None
    while not to_exit:
        turn, bungee_mode = gameModule.get_some_variables()
        if turn == global_turn:
            min_player_index, min_score, players_score = gameModule.do_end()
            print(f"Player {min_player_index + 1} is the winner!!   his score - {min_score}   all the players scores are - {players_score}")
            gameModule.do_break()
        print(f"Player number {turn + 1}")
        print(f"Bungee mode is: {bungee_mode}")
        print(gameModule.get_state(True))
        choice = input(" Enter your choice: ")
        if choice == "Q":
            gameModule.do_break()
        elif choice == "B":
            global_turn = turn
            gameModule.do_bungee()
        else:
            to_throw = list(choice[:-1])
            to_throw = [int(i) for i in to_throw]
            if choice[-1] == "T":
                from_stack = True
            else:
                from_stack = False
            stick = gameModule.do_game(to_throw, from_stack)
            if stick:
                print("Oh no!!! You cant stick!!")
            if stick is False:
                print("Oh Yeh!!! You stick!!")
            print("")
            print(gameModule.get_state(False))
        print("====================================")


game(3)
