class GameLogo(object):
    def logo(self):
        print(f"\033[1;33;40m\033")
        print("""

    | |  | |                                  / _| | |  | |           |  __ \                  | |
    | |__| |  ___   _   _  ___   ___    ___  | |_  | |_ | |__    ___  | |  | |  ___   __ _   __| |
    |  __  | / _ \ | | | |/ __| / _ \  / _ \ |  _| | __|| '_ \  / _ \ | |  | | / _ \ / _` | / _` |
    | |  | || (_) || |_| |\__ \|  __/ | (_) || |   | |_ | | | ||  __/ | |__| ||  __/| (_| || (_| |
    |_|  |_| \___/  \__,_||___/ \___|  \___/ |_|    \__||_| |_| \___| |_____/  \___| \__,_| \__,_|
           """)
        print('\033[39m')


if __name__ == "__main__":
    obj = GameLogo()
    obj.logo()

