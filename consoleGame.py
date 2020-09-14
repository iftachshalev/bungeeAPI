from Maneger import Manager


def repeat(gameModule, to_turn=None):
    turn, bungee_mode = gameModule.get_some_variables()
    print(f"Player number {turn + 1}")
    print(f"Bungee mode is: {bungee_mode}")
    print(gameModule.get_state(True))
    choice = input(" Enter your choice: ")
    if choice == "Q":
        gameModule.do_break()
    elif choice != "B":
        to_throw = list(choice[:-1])
        to_throw = [int(i) for i in to_throw]
        if choice[-1] == "T":
            from_stack = True
        else:
            from_stack = False
        success = False
        while not success:
            success = gameModule.do_game(to_throw, from_stack, to_turn)
        print(gameModule.get_state(False))
        print("====================================")
    return choice


def game(num):
    gameModule = Manager(num)
    to_exit = False
    while not to_exit:
        choice = repeat(gameModule)
        if choice == "B":
            gameModule.do_bungee()
            turn, bungee_mode = gameModule.get_some_variables()
            v1 = repeat(gameModule, (turn + 1) % num)
            for i in range(num - 2):
                v1 = repeat(gameModule)
            minplayer_index, minscore, players_score = gameModule.do_end()
            print("")
            print(f"Player Number: {minplayer_index + 1} Is The Winner!!!!!!!!!!!!!!!!")
            print(f"his score - {minscore}")
            print(f"all the scores - {players_score}")
            to_exit = True


game(2)
