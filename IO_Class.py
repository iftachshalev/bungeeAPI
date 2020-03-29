

class IO_Class:

    def __init__(self):
        self.file_flag = None
        self.screen_flag = None
        self.url = ""
        self.file = open(self.url, "W")

    def print(self, what_to_print):
        if self.file_flag and self.screen_flag:
            print(what_to_print)
            self.file.write(what_to_print)
        elif self.file_flag and not self.screen_flag:
            self.file.write(what_to_print)
        elif self.screen_flag and not self.file_flag:
            print(what_to_print)

    def close(self):
        self.file.close()