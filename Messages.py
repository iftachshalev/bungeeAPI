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

        self.array = [i for i in args]
        if type(self.array[0]) == list:
            for i in self.array:
                self.array = self.array[0]

    def encode(self) -> bytes:
        var = str(self.array[0])
        for i in range(1, len(self.array)):
            var += self.DELIM
            var += str(self.array[i])

        return var.encode()

    @staticmethod
    def decode(data: bytes):
        array = data.split(StartGameMessage.DELIM.encode())
        ar = [int(i.decode()) for i in array]
        return StartGameMessage(ar[:])


