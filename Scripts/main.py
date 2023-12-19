from game_logo import GameLogo
from new_game import NewGame
from slow_print import SlowPrint


class HouseOfTheDead(object):
    def __init__(self):
        self.logo = GameLogo()
        self.new_game = NewGame()
        self.slow_print = SlowPrint()

    def main(self):
        self.logo.logo()
        scenario = ("""
           SCENARIO :-
           It's Halloween night and you happen to discover an abandoned house. 
           You thought it to be a fun haunted house but it turns out to be a real haunted house with zombies and 
           spirits. You need to find the way out of the house as soon as possible !!!! 
           But you are completely unaware about the dangers that lay ahead. I'm the voice in your head  and will guide 
           you throughout. However, remember, one silly move and you are DEAD!!!
        """)
        self.slow_print.print_slow(scenario)
        self.new_game.start_game()


if __name__ == "__main__":
    obj = HouseOfTheDead()
    obj.main()