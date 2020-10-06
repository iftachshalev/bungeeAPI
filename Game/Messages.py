

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
                        t = []
                        str = i[1:-1]
                        if str[0] == "[" and str[-1] == "[":
                            str = str[1:-1]
                        str = str.split(", ")
                        for i in range(len(str)):
                            try:
                                t.append(int(str[i]))
                            except:
                                t.append(str[i])
                        array.append(t)

        return StartGameMessage(array[:])


# t1 = [1, 2, [10, 6, 4, 3], 3, [5, 5, False]]
# t2 = []
# ddd = StartGameMessage(t1[:])
# s1 = ddd.encode()
# print(s1)
#
# prin = StartGameMessage().decode(s1).array
# print(prin)


