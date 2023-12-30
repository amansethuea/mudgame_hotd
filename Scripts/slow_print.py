from time import sleep
import os


class SlowPrint(object):
    def print_slow(self, txt):
        for x in txt:                     # cycle through the text one character at a time
            print(x, end='', flush=True)  # print one character, no new line, flush buffer
            sleep(0.01)
        print()  # go to new line

    def check_dir_file_exists(self, dir_name, file_name):
        if os.path.isfile(f"../{dir_name}/{file_name}"):
            file_path = f"../{dir_name}/{file_name}"
            return file_path
        elif os.path.isfile(f"../mudgame_hotd/{dir_name}/{file_name}"):
            file_path = f"../mudgame_hotd/{dir_name}/{file_name}"
            return file_path
        elif os.path.isfile(f"../../mudgame_hotd/{dir_name}/{file_name}"):
            file_path = f"../../mudgame_hotd/{dir_name}/{file_name}"
            return file_path
        else:
            return f"{file_name} not found"


if __name__ == "__main__":
    obj = SlowPrint()
