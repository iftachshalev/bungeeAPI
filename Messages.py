# class Message:
#     pass
#
#
# class StartGameMessage:
#
#     DELIM = ":-)"
#
#     def __init__(self, my_turn, lucky_card):
#         self.my_turn = my_turn
#         self.lucky_card = lucky_card
#
#     def encode(self) -> bytes:
#         return (str(self.my_turn) + self.DELIM + str(self.lucky_card)).encode()
#
#     @staticmethod
#     def decode(data: bytes):
#         array = data.split(StartGameMessage.DELIM.encode())
#         return StartGameMessage(int(array[0].decode()), int(array[1].decode()))
#

class StartGameMessage:

    DELIM = ":-)"

    def __init__(self, *args):
        #if type(args[0]) == list:
        try:
            self.array = [i for i in args]
            if type(self.array[0]) == list:
                for i in self.array:
                    self.array = self.array[0]
        except:
            self.array = args

    def encode(self) -> bytes:
        var = str(self.array[0])
        for i in range(1, len(self.array)):
            var += self.DELIM
            var += str(self.array[i])

        return var.encode()

    @staticmethod
    def decode(data: bytes):
        array = data.split(StartGameMessage.DELIM.encode())
        ar = [i.decode() for i in array]
        array = []
        for i in ar:
            try:
                e = int(i)
                array.append(e)
            except ValueError:

                # first_list_of_array = list(i)
                # arbif = []
                # for i in first_list_of_array:
                #     try:
                #         int(i)
                #         arbif.append(int(i))
                #     except:
                #         pass
                # len_arbif = len(arbif)
                # min_array_to_array = []
                # if_jump = False
                # for index, vul in enumerate(ar):
                #     if if_jump:
                #         if_jump = False
                #     else:
                #         if len_arbif > 5 and vul == 1 and arbif[index + 1] == 0:
                #             min_array_to_array.append(10)
                #             len_arbif -= 1
                #             if_jump = True
                #
                #         else:
                #             min_array_to_array.append(vul)
                #
                # array.append(min_array_to_array)
                # print(min_array_to_array)

                first_str_array = list(i)
                first_int_array = []
                for i in first_str_array:
                    try:
                        int(i)
                        first_int_array.append(int(i))
                    except:
                        pass
                len_first_int_array = len(first_int_array)
                the_real_array_cards = []
                if_jump = False
                for index, vul in enumerate(first_int_array):
                    if if_jump:
                        if_jump = False
                    else:
                        if len_first_int_array > 5 and vul == 1 and first_int_array[index + 1] == 0:
                            the_real_array_cards.append(10)
                            len_first_int_array -= 1
                            if_jump = True

                        else:
                            the_real_array_cards.append(vul)

                array.append(the_real_array_cards)
        return StartGameMessage(array[:])


# ddd = StartGameMessage(1, 2, [2, 4, 4, 9, 10], 9)
# s1 = ddd.encode()
# print(s1)
#
# prin = StartGameMessage().decode(s1).array
# print(prin)
#
#
