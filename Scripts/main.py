from game_logo import GameLogo
from new_game import NewGame


class HouseOfTheDead(object):
    def __init__(self):
        self.logo = GameLogo()
        self.new_game = NewGame()

    def main(self):
        self.logo.logo()
        print("""
           SCENARIO :-
           It's Halloween night and you happen to discover an abandoned house. 
           You thought it to be a fun haunted house but it turns out to be a real haunted house with zombies and 
           spirits. You need to find the way out of the house as soon as possible !!!! 
           But you are completely unaware about the dangers that lay ahead. I'm the voice in your head  and will guide 
           you throughout. However, remember, one silly move and you are DEAD!!!
        """)
        self.new_game.start_game()


if __name__ == "__main__":
    obj = HouseOfTheDead()
    obj.main()

"""
Code references:-
Colour text: https://ozzmaker.com/add-colour-to-text-in-python/
Progress Bar: https://medium.com/pythoniq/progress-bars-in-python-with-progressbar2-da77838077a9
Move Counter: https://stackoverflow.com/questions/54714945/create-a-function-that-will-increment-by-one-when-called
csv writer / reader: https://docs.python.org/3/library/csv.html
datetime: https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
Fonts: https://patorjk.com/software/taag/#p=testall&h=1&v=3&f=Ghost&t=House%20of%20the%20Dead
csv dict reader: https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
re module: https://www.geeksforgeeks.org/python-extract-numbers-from-string/
"""
