import os



class IO_Class:

    def __init__(self, url, file_flag, screen_flag, from_func):
        self.file_flag = file_flag
        self.screen_flag = screen_flag
        self.from_func = from_func
        self.url = url
        self.turn = None
        self.file = open(self.url, "a")

    def my_func(self, the_ask):
        return "4T"

    def print(self, what_to_print):
        if self.file_flag:
            self.file.write(what_to_print + '\n')
        if self.screen_flag:
            print(what_to_print)

    def close(self):
        self.file.close()

    def delete_file(self):
        self.file.close()
        os.remove("iftachshalev30115com.txt")

    def get_turn(self, what_to_ask):
        if self.from_func:
            self.turn = self.my_func(what_to_ask)
        else:
            self.turn =input("Action:  B [Bungee]  Q [Quit]\n>>>")

d = IO_Class("iftachshalev30115com.txt", True, True, True)
d.print("iftach hatotach")
d.print("qrtqrtafgafg5")
d.delete_file()
d.close()