import sys
import time
import progressbar
from character_creation import CharacterCreation
from locations import Locations
from saving_loading import SaveLoadProcess
from slow_print import SlowPrint


class NewGame(object):
    def __init__(self):
        self.new_player_data = CharacterCreation()
        self.locations = Locations(1)
        self.save_load = SaveLoadProcess()
        self.slow_print = SlowPrint()

    def progress_bar(self):
        loop_count = 100
        with progressbar.ProgressBar(max_value=loop_count) as bar:
            for i in range(loop_count):
                bar.update(i)
                time.sleep(0.01)

    def start_game(self):
        while True:
            print(f"\033[1;37;40m\033")
            game_type = input("Do you wish to play new game or load saved game? Please enter new or load: ")
            game_type_upper = game_type.upper()
            if game_type_upper in ["NEW", "LOAD", "END"]:
                if game_type_upper == "NEW":
                    self.slow_print.print_slow("Setting up new game for you. Please wait")
                    self.progress_bar()
                    player_data_dict = self.new_player_data.save_new_player_data()
                    level = True
                    while level:
                        difficulty_level = input("Please chose a difficulty level: Beginner / Intermediate / Expert: ")
                        if (difficulty_level in
                                ["Beginner", "beginner", "BEGINNER", "Intermediate", "intermediate", "INTERMEDIATE",
                                 "Expert", "expert", "EXPERT"]):
                            get_file = self.slow_print.check_dir_file_exists("Resources", "level.txt")
                            fo = open(get_file, "a")
                            fo.write("\n")
                            fo.write(player_data_dict['user_id'] + "," + difficulty_level)
                            fo.close()
                            level = False
                            print('\033[39m')
                            self.locations.deadly_dining_hall(player_data_dict)
                        else:
                            print(f"\033[1;37;40m\033")
                            self.slow_print.print_slow("Invalid difficulty level. Please enter again "
                                                       "out of: Beginner / Intermediate / Expert")
                            print('\033[39m')
                    break
                elif game_type_upper == "END":
                    print(f"\033[1;37;40m\033")
                    self.slow_print.print_slow("It's sad you chose not to play. See you next time!")
                    print('\033[39m')
                    sys.exit(0)
                elif game_type_upper == "LOAD":
                    print(f"\033[1;37;40m\033")
                    user_id = input("Please enter your existing User ID: ")
                    self.slow_print.print_slow("Hang on! We are bringing back your favourite MUD game.")
                    print('\033[39m')
                    self.save_load.load_game(user_id)
                    break
                else:
                    self.slow_print.print_slow("Invalid Input. Please enter valid input.")
            else:
                self.slow_print.print_slow("Invalid input entered. Please enter a valid input. "
                                           "Expected inputs are either 'new' or 'load'.")


if __name__ == "__main__":
    obj = NewGame()