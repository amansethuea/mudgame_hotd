import sys
import time
import progressbar
from character_creation import CharacterCreation
from locations import Locations
from saving_loading import SaveLoadProcess


class NewGame(object):
    def __init__(self):
        self.new_player_data = CharacterCreation()
        self.locations = Locations(1)
        self.save_load = SaveLoadProcess()

    def progress_bar(self):
        loop_count = 100
        with progressbar.ProgressBar(max_value=loop_count) as bar:
            for i in range(loop_count):
                bar.update(i)
                time.sleep(0.01)

    def start_game(self):
        game_type = input("Do you wish to play new game or load saved game? Please enter new or load: ")
        game_type_upper = game_type.upper()
        if game_type_upper in ["NEW", "LOAD", "END"]:
            if game_type_upper == "NEW":
                print("Setting up new game for you. Please wait")
                self.progress_bar()
                player_data_dict = self.new_player_data.save_new_player_data()
                self.locations.deadly_dining_hall(player_data_dict)
            elif game_type_upper == "END":
                print("It's sad you chose not to play. See you next time!")
                sys.exit(0)
            elif game_type_upper == "LOAD":
                user_id = input("Please enter your existing User ID: ")
                print("Hang on! We are bringing back your favourite MUD game.")
                self.save_load.load_game(user_id)
            else:
                print("Invalid Input. Please enter valid input.")
        else:
            print("Invalid input entered. Please enter a valid input. Expected inputs are either 'new' or 'load'.")


if __name__ == "__main__":
    obj = NewGame()