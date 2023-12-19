import sys
import os.path


class CharacterCreation(object):
    def save_new_player_data(self):
        while True:
            new_player_data_dict = self.character_creation()
            check_file = os.path.isfile("../Resources/player_info.txt")
            if check_file:
                user_id_available = True
                player_read_file = open("../Resources/player_info.txt", "r")
                player_data_list = player_read_file.readlines()
                if player_data_list[1:]:
                    for player in player_data_list[1:]:
                        player_list = player.split(",")
                        if new_player_data_dict['user_id'] == player_list[2]:
                            user_id_available = False
                    if user_id_available:
                        player_read_file.close()
                        player_write_file = open("../Resources/player_info.txt", "a")
                        complete_info = (f"{new_player_data_dict['name']},{new_player_data_dict['age']},"
                                        f"{new_player_data_dict['user_id']},{new_player_data_dict['char']}")
                        player_write_file.write("\n")
                        player_write_file.write(complete_info)
                        player_write_file.close()
                        print(f"Awesome! New character created for "
                            f"{new_player_data_dict['name']} /  {new_player_data_dict['user_id']}")
                        print("Let's begin the haunted adventure.")
                        return new_player_data_dict
                    else:
                        print(
                            f"The user ID {new_player_data_dict['user_id']} is already taken. "
                            f"Please use a different User ID.")
                        player_read_file.close()
                else:
                    print("Great! Saving's first ever HOTD player's information.")
                    player_write_file = open("../Resources/player_info.txt", "w+")
                    player_write_file.write('Name,Age,UserID,Character\n')
                    complete_info = (f"{new_player_data_dict['name']},{new_player_data_dict['age']},"
                                    f"{new_player_data_dict['user_id']},{new_player_data_dict['char']}")
                    player_write_file.write(complete_info)
                    player_write_file.close()
                    print(f"Awesome! New character created for "
                        f"{new_player_data_dict['name']} /  {new_player_data_dict['user_id']}")
                    print("Let's begin the haunted adventure. But first, one last step :) ")
                    return new_player_data_dict
            else:
                print("player_info.txt doesn't exist. Exiting")
                sys.exit(0)

    def character_creation(self):
        print("PLAYERS INFORMATION")
        player_name = input("Enter your name: ")
        player_age = input("Enter your age: ")
        player_user_id = input("Enter your user id: ")

        while True:
            print("CHARACTER SELECTION")
            choose_char = input("Chose a character from the following: Nick, Tom, Mario, Luigi, Sonic: ")
            convert_to_upper = choose_char.upper()

            if convert_to_upper not in ["NICK", "TOM", "MARIO", "LUIGI", "SONIC"]:
                print("Invalid character selection. Re-try again.")
            else:
                player_data_dict = {"name": player_name, "age": player_age, "user_id": player_user_id,
                                    "char": choose_char}
                return player_data_dict
            break


if __name__ == "__main__":
    obj = CharacterCreation()