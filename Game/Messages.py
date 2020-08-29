

class StartGameMessage:

    DELIM = ":-)"

    def __init__(self, *args):

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
            if i != "":
                try:
                    e = int(i)
                    array.append(e)
                except ValueError:

                    if i[0] != "[":
                        array.append(i)
                    else:
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


# ddd = StartGameMessage("fdghrth", "dvbvfsddd", "rrrrrr")
# s1 = ddd.encode()
# print(s1)
#
# prin = StartGameMessage().decode(s1).array
# print(prin)
#

