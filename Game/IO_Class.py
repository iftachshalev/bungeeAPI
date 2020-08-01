from UI.ClientClass import Client
from Game.Messages import StartGameMessage


class IO_Class:

    def __init__(self, file_flag, screen_flag, url='', conn=None):
        self.file_flag = file_flag
        self.screen_flag = screen_flag
        self.url = url
        self.turn = None
        if url != '':
            self.file = open(self.url, "w")
        self.conn = conn
        self.with_data = True

    def print(self, what_to_print):
        if self.file_flag:
            self.file.write(what_to_print + '\n')

        if self.screen_flag:
            print(what_to_print)

        if self.conn:
            ddd = StartGameMessage(what_to_print)
            s1 = ddd.encode()
            # s2 = ddd.decode(s1).array
            # print(s2)
            self.conn.sendall(s1)
            ack = self.conn.recv(1024)
            if ack != b"ack":
                raise ConnectionError("ack is'nt receive")

        #     ddd = StartGameMessage(33, 4445, 665, 8767)
        #     s1 = ddd.encode()
        #     print(s1)
        #     s2 = ddd.decode(s1).array
        #     print(s2)



    def close(self):
        if self.url != '':
            self.file.close()


class Input:

    def __init__(self, conn=None, user_funcs=None):
        self.user_funcs = user_funcs
        self.conn = conn

    def get_turn(self, my_cards, lucky_card, lost_card, bungee_mode, score):
        if self.user_funcs:
            my_func = self.user_funcs
            return my_func(my_cards, lucky_card, lost_card, bungee_mode, score)
        else:
            if self.conn:
                StartGameMessag = StartGameMessage("I")
                self.conn.sendall(StartGameMessag.encode())
                ack = self.conn.recv(1024)
                if ack != b"ack":
                    raise ConnectionError("ack is'nt receive")
                StartGameMessag = StartGameMessage(" Action:  B [Bungee]  Q [Quit]\n >>>")
                self.conn.sendall(StartGameMessag.encode())
                what_to_do = self.conn.recv(1024).StartGameMessage().decode().array
            else:
                what_to_do = input(" Action:  B [Bungee]  Q [Quit]\n >>>")

            say_bungee = False
            from_stack = True
            to_quit = False
            throw_card = []
            error_msg = ''
            if what_to_do == '':
                error_msg = 'Error: empty command'
            elif what_to_do == "B":
                if score <= 5:
                    say_bungee = True
                else:
                    error_msg = 'Error: score > 5, cant say bungee'
            elif what_to_do == "Q":
                to_quit = True
            elif len(what_to_do) >= 2 & len(what_to_do) < len(my_cards)+1:
                is_from_stack = what_to_do[-1]
                if is_from_stack == "T":
                    from_stack = True
                elif is_from_stack == "F":
                    from_stack = False
                else:
                    error_msg = "Error: Invalid text, pleas try again"

                try:
                    for i in range(len(what_to_do[:-1])):
                        tcard = int(what_to_do[i])
                        if tcard > len(my_cards)-1:
                            error_msg = 'Error: index not in cards'
                        else:
                            throw_card.append(tcard)
                except Exception as e:
                    error_msg = repr(e)
            else:
                error_msg = 'Error: command not understood'

            dict = {
                'say_bungee': say_bungee,
                'from_stack': from_stack,
                'quit': to_quit,
                'error': error_msg,
                'throw_cards': throw_card
            }

            return dict
            # validation from user

    # def input_num_users(self, robot_users):
    #     if self.from_func:
    #         return robot_users
    #     else:
    #         return int(input("Choose Number Of Players:"))


# d = IO_Class(True, True, "f1.txt")
# d.print("hello world 123")
# d.print("nadav shalev 321")
# d.close()

# def my_func(my_cards, lucky_card, lost_card, bungee_mode, score):
#     return "4T"
#
#
# funcs = {
#     0: algo_simple,
#     1: my_func
# }
#
# inp = Input(False)
#
# print(inp.get_turn(1, 1, 1, 1, 1, 1))
#
# res_turn = inp.get_turn(0, [2, 3, 5, 7, 8], 9, 8, False, 25)
# print(res_turn)
# res_turn = inp.get_turn(1, [2, 3, 5, 7, 8], 9, 8, False, 25)
# print(res_turn)

d = IO_Class(False, False)
d.print("33")
