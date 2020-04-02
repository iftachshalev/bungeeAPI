import os
from nadavAlgo import *


class IO_Class:

    def __init__(self, file_flag, screen_flag, url=''):
        self.file_flag = file_flag
        self.screen_flag = screen_flag
        self.url = url
        self.turn = None
        if url != '':
            self.file = open(self.url, "a")
            # clear file before use

    def print(self, what_to_print):
        if self.file_flag:
            self.file.write(what_to_print + '\n')
        if self.screen_flag:
            print(what_to_print)

    def close(self):
        if self.url != '':
            self.file.close()

    def delete_file(self):
        self.file.close()
        os.remove("iftachshalev30115com.txt")


class Input:

    def __init__(self, from_func, user_funcs=None):
        self.from_func = from_func
        self.user_funcs = user_funcs

    def get_turn(self, turn, my_cards, lucky_card, lost_card, bungee_mode, score):
        if self.from_func:
            my_func = self.user_funcs[turn]
            return my_func(my_cards, lucky_card, lost_card, bungee_mode, score)
        else:
            return input("Action:  B [Bungee]  Q [Quit]\n>>>")
            # validation from user

# d = IO_Class("iftachshalev30115com.txt", True, True, True)
# d.print("iftach hatotach")
# d.print("qrtqrtafgafg5")
# d.delete_file()
# d.close()

def my_func(my_cards, lucky_card, lost_card, bungee_mode, score):
    return "4T"


funcs = {
    0: algo_simple,
    1: my_func
}

inp = Input(True, funcs)

res_turn = inp.get_turn(0, [2, 3, 5, 7, 8], 9, 8, False, 25)
print(res_turn)
res_turn = inp.get_turn(1, [2, 3, 5, 7, 8], 9, 8, False, 25)
print(res_turn)



