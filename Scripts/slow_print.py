from time import sleep


class SlowPrint(object):
    def print_slow(self, txt):
        for x in txt:                     # cycle through the text one character at a time
            print(x, end='', flush=True)  # print one character, no new line, flush buffer
            sleep(0.01)
        print()  # go to new line


if __name__ == "__main__":
    obj = SlowPrint()