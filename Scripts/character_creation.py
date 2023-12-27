import sys
from slow_print import SlowPrint
from pygame import mixer


class CharacterCreation(object):

    def __init__(self):
        self.slow_print = SlowPrint()

    def save_new_player_data(self):
        new_player_data_dict = self.character_creation()
        get_file = self.slow_print.check_dir_file_exists("Resources", "player_info.txt")
        if get_file not in "not found":
            user_id_available = True
            player_read_file = open(get_file, "r")
            player_data_list = player_read_file.readlines()
            if player_data_list[1:]:
               
                for player in player_data_list[1:]:
                    player_list = player.split(",")
                    if len(player_list)==1:
                        continue
                    if new_player_data_dict['user_id'] == player_list[2]:
                        user_id_available = False

                if user_id_available:
                    player_read_file.close()
                    player_write_file = open(get_file, "a")

                    complete_info = (f"{new_player_data_dict['name']},{new_player_data_dict['age']},"
                                     f"{new_player_data_dict['user_id']},{new_player_data_dict['char']}")
                    player_write_file.write("\n")
                    player_write_file.write(complete_info)
                    player_write_file.close()
                    self.slow_print.print_slow(f"Awesome! New character created for "
                                               f"{new_player_data_dict['name']} /  {new_player_data_dict['user_id']}")
                    self.slow_print.print_slow("Let's begin the haunted adventure. But first, one last step :) ")
                    return new_player_data_dict
                else:
                    self.slow_print.print_slow(
                        f"The user ID {new_player_data_dict['user_id']} is already taken. "
                        f"Please use a different User ID.")
                    player_read_file.close()
                    sys.exit(0)
            else:
                self.slow_print.print_slow("Great! Saving's first ever HOTD player's information.")
                player_write_file = open(get_file, "w+")
                player_write_file.write('Name,Age,UserID,Character\n')
                complete_info = (f"{new_player_data_dict['name']},{new_player_data_dict['age']},"
                                 f"{new_player_data_dict['user_id']},{new_player_data_dict['char']}")
                player_write_file.write(complete_info)
                player_write_file.close()
                self.slow_print.print_slow(f"Awesome! New character created for "
                                           f"{new_player_data_dict['name']} /  {new_player_data_dict['user_id']}")
                self.slow_print.print_slow("Let's begin the haunted adventure.")
                return new_player_data_dict
        else:
            self.slow_print.print_slow("player_info.txt doesn't exist. Exiting")
            sys.exit(0)

    def character_creation(self):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio","horror-ambience.wav"))
        mixer.music.play()
        self.slow_print.print_slow("PLAYERS INFORMATION")

        def has_numbers(input_string):
            return any(char.isdigit() for char in input_string)

        while True:
            player_name = input("Enter your name: ")
            if has_numbers(player_name):
                self.slow_print.print_slow(f"{player_name} contains numeric values. Please make sure name only "
                                           f"contains alphabets")
            else:
                break

        def has_alphabets(input_string):
            return any(char.isalpha() for char in input_string)

        while True:
            player_age = input("Enter your age: ")
            if has_alphabets(player_age):
                self.slow_print.print_slow(f"{player_age} contains alphabetical values. Please make sure age only "
                                           f"contains numbers between 3 - 99")
            elif int(player_age) < 3 or int(player_age) > 99:
                self.slow_print.print_slow(f"{player_age} can only be between 3 - 99")
            else:
                break

        while True:
            player_user_id = input("Enter your user id: ")
            if len(player_user_id) < 3 or len(player_user_id) > 15:
                self.slow_print.print_slow(f"The length of user ID should be between range 3-15. Please try again")
            else:
                break

        while True:
            self.slow_print.print_slow("CHARACTER SELECTION")
            choose_char = input("Chose a character from the following: Nick, Tom, Mario, Luigi, Sonic: ")
            convert_to_upper = choose_char.upper()

            if convert_to_upper not in ["NICK", "TOM", "MARIO", "LUIGI", "SONIC"]:
                self.slow_print.print_slow("Invalid character selection. Re-try again.")
            else:
                player_data_dict = {"name": player_name, "age": player_age, "user_id": player_user_id,
                                    "char": choose_char}
                return player_data_dict


if __name__ == "__main__":
    obj = CharacterCreation()
    obj.character_creation()