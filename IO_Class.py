import os



class IO_Class:

    def __init__(self, url, file_flag, screen_flag, from_func):
        self.file_flag = file_flag
        self.screen_flag = screen_flag
        self.from_func = from_func
        self.url = url
        self.file = open(self.url, "a")

    def print(self, what_to_print):
        if self.file_flag:
            self.file.write(what_to_print + '\n')
        if self.screen_flag:
            print(what_to_print)

    def close(self):
        self.file.close()

    def delete_file(self):
        os.remove(self.url)

    def get_turn(self, what_to_ask):
        pass

d = IO_Class("iftachshalev30115com.txt", True, True, True)
d.print("iftach hatotach")
d.print("qrtqrtafgafg5")
d.close()