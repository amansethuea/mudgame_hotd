import os.path
import sys
import time
import progressbar
import random
import csv
import re
from itertools import count
from datetime import datetime


class HouseOfTheDead(object):
    def __init__(self):
        self.counter = count(1)

    def main(self):
        print(f"\033[1;33;40m\033")
        self.logo()
        print("""
           SCENARIO :-
           It's Halloween night and you happen to discover an abandoned house. 
           You thought it to be a fun haunted house but it turns out to be a real haunted house with zombies and 
           spirits. You need to find the way out of the house as soon as possible !!!! 
           But you are completely unaware about the dangers that lay ahead. I'm the voice in your head  and will guide 
           you throughout. However, remember, one silly move and you are DEAD!!!
        """)
        self.start_game()

    def logo(self):
        print("""
                                                                        
 | |  | |                                  / _| | |  | |           |  __ \                  | |
 | |__| |  ___   _   _  ___   ___    ___  | |_  | |_ | |__    ___  | |  | |  ___   __ _   __| |
 |  __  | / _ \ | | | |/ __| / _ \  / _ \ |  _| | __|| '_ \  / _ \ | |  | | / _ \ / _` | / _` |
 | |  | || (_) || |_| |\__ \|  __/ | (_) || |   | |_ | | | ||  __/ | |__| ||  __/| (_| || (_| |
 |_|  |_| \___/  \__,_||___/ \___|  \___/ |_|    \__||_| |_| \___| |_____/  \___| \__,_| \__,_|
        """)

    def check_header_existence(self, file_name):
        fo = open(file_name, 'r')
        data = fo.readlines()
        for lines in data:
            lines = lines.split(",")
            if lines[0] == "Name":
                return True
            else:
                return False

    def save_progress(self, player_data, location):
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('current_game_progress_info.txt', 'a', newline='\n') as csvfile:
            write_current_progress = csv.writer(csvfile, delimiter=',')
            if location in ["escape_door"]:
                game_completion = "T"
                self.leaderboard(player_data)
            else:
                game_completion = "F"
            if self.check_header_existence('current_game_progress_info.txt'):
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 self.counter, location, date_time, game_completion])
            else:
                write_current_progress.writerow(["Name", "UserID", "Character", "Moves", "CurrentLocation", "Date&Time",
                                                 "GameCompletion"])
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 self.counter, location, date_time, game_completion])
            csvfile.close()

    def get_move_counter_for_load_game(self, moves_count_str):
        get_current_moves_str = moves_count_str
        get_current_moves_list = re.findall(r'\d+', get_current_moves_str)
        if len(get_current_moves_list) > 1:
            get_move_count_str = ''.join(get_current_moves_list)
            get_move_count = int(get_move_count_str)
        else:
            get_move_count = int(get_current_moves_list[0])
        return get_move_count

    def load_game(self, user_id):
        get_user_dict = {}
        with open('current_game_progress_info.txt', 'r') as data:
            for line in csv.DictReader(data):
                for attr, val in line.items():
                    if attr == 'UserID':
                        if user_id == val:
                            if line['GameCompletion'] == 'F' and line['CurrentLocation'] not in (
                                    'escape_door', 'heaven'):
                                get_user_dict = line
            data.close()
        if get_user_dict:
            # Forming player_data dict. Giving a random age as age is not used anywhere other than player_info.txt
            player_data = {"name": get_user_dict["Name"], "age": 20, "user_id": get_user_dict["UserID"],
                           "char": get_user_dict["Character"]}
            print(f"Please wait. Loading game for user {get_user_dict['UserID']}")
            self.progress_bar()
            if get_user_dict['CurrentLocation'] == 'deadly_dining_hall':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                self.counter = count(get_move_count)
                self.deadly_dining_hall(player_data)
            elif get_user_dict['CurrentLocation'] == 'haunted_hallway':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                self.counter = count(get_move_count)
                self.haunted_hallway(player_data)
            elif get_user_dict['CurrentLocation'] == 'chilling_corridor':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                self.counter = count(get_move_count)
                self.chilling_corridor(player_data)
            elif get_user_dict['CurrentLocation'] == 'sinister_stairway':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                self.counter = count(get_move_count)
                self.sinister_stairway(player_data)
            else:
                print("Invalid Location")
        else:
            print(f"{user_id} user not found. Please start a new game.")

    def progress_bar(self):
        loop_count = 100
        with progressbar.ProgressBar(max_value=loop_count) as bar:
            for i in range(loop_count):
                bar.update(i)
                time.sleep(0.01)

    def leaderboard(self, player_data):
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('leaderboard.txt', 'a', newline='\n') as csvfile:
            write_current_progress = csv.writer(csvfile, delimiter=',')
            if self.check_header_existence('leaderboard.txt'):
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 self.counter, date_time])
            else:
                write_current_progress.writerow(["Name", "UserID", "Character", "Moves", "Date&Time"])
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 self.counter, date_time])
            csvfile.close()

    def start_game(self):
        game_type = input("Do you wish to play new game or load saved game? Please enter new or load: ")
        game_type_upper = game_type.upper()
        if game_type_upper in ["NEW", "LOAD", "END"]:
            if game_type_upper == "NEW":
                print("Setting up new game for you. Please wait")
                self.progress_bar()
                player_data_dict = self.save_new_player_data()
                self.deadly_dining_hall(player_data_dict)
            elif game_type_upper == "END":
                print("It's sad you chose not to play. See you next time!")
                sys.exit(0)
            elif game_type_upper == "LOAD":
                user_id = input("Please enter your existing User ID: ")
                print("Hang on! We are bringing back your favourite MUD game.")
                self.load_game(user_id)
            else:
                print("Invalid Input. Please enter valid input.")
        else:
            print("Invalid input entered. Please enter a valid input. Expected inputs are either 'new' or 'load'.")

    def save_new_player_data(self):
        new_player_data_dict = self.character_creation()
        check_file = os.path.isfile("player_info.txt")
        if check_file:
            user_id_available = True
            player_read_file = open("player_info.txt", "r")
            player_data_list = player_read_file.readlines()
            if player_data_list[1:]:
                for player in player_data_list[1:]:
                    player_list = player.split(",")
                    if new_player_data_dict['user_id'] == player_list[2]:
                        user_id_available = False

                if user_id_available:
                    player_read_file.close()
                    player_write_file = open("player_info.txt", "a")
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
                    sys.exit(0)
            else:
                print("Great! Saving's first ever HOTD player's information.")
                player_write_file = open("player_info.txt", "w+")
                player_write_file.write('Name,Age,UserID,Character\n')
                complete_info = (f"{new_player_data_dict['name']},{new_player_data_dict['age']},"
                                 f"{new_player_data_dict['user_id']},{new_player_data_dict['char']}")
                player_write_file.write(complete_info)
                player_write_file.close()
                print(f"Awesome! New character created for "
                      f"{new_player_data_dict['name']} /  {new_player_data_dict['user_id']}")
                print("Let's begin the haunted adventure.")
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

    def dead(self, player_data):
        print("\nYou push some unwanted door, it creeks as it opens.")
        print("This is a very strange, dark place, but you walk in.")
        print("The door slams shut !!\n")
        print("ZOMBIES !!!\n")
        print("You're ...DEAD !!\n")
        print("I warned you not go that way.")
        print(f"Oh dear {player_data['name']}. Never mind. Do you wish to play again?")
        play_again = input('Type "YES" (and press ENTER) to play again, or just press ENTER to end the program. \n')
        if play_again in ["YES", "yes", "Yes"]:
            self.deadly_dining_hall(player_data)
        else:
            print("Thank you for playing the HOTD. See you next time!")
            self.save_progress(player_data, "heaven")
            sys.exit(0)

    def deadly_dining_hall(self, player_data):
        print()
        print("You are in the main dining hall of the haunted house, standing alone, in the dark.")
        print("You see three ways to go.")
        print("Do you go to the north (N), south (S) or east (E)?.")
        print("BEWARE!!! DO NOT go to go the West")
        print("Remember you can type Save/save the game at any point.")
        print()
        choice = input("Enter either N/North, S/South or E/East: ")
        choice = choice.upper()
        if choice in ["N", "NORTH"]:
            print(f"Moves: {next(self.counter)}")
            self.haunted_hallway(player_data)
        elif choice in ["S", "SOUTH"]:
            print(f"Moves: {next(self.counter)}")
            self.chilling_corridor(player_data)
        elif choice in ["E", "EAST"]:
            print(f"Moves: {next(self.counter)}")
            self.sinister_stairway(player_data)
        elif choice in ["W", "WEST"]:
            print(f"Moves: {next(self.counter)}")
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress(player_data, "deadly_dining_hall")
        else:
            print("I did not understand that. Let's try again. HURRY! You have to get out now!!")
            print(f"Moves: {next(self.counter)}")
            self.deadly_dining_hall(player_data)

    def haunted_hallway(self, player_data):
        print("You are in a creepy hallway where zombies are roaming looking for prey to suck blood out of them")
        print("You notice there are ways to the north (N) and south (S).")
        print("BEWARE!!! DO NOT go to go the West (W) or East (E) if you don't wish to die the most painful death.")
        print("Remember you can type Save/save the game at any point.")
        print()
        choice = input("Enter either N/North or S/South: ")
        choice = choice.upper()
        if choice in ["N", "NORTH"]:
            print()
            print("Oh! you have found the escape door. But it's locked")
            print("There is a key in one of the locations of the house to un-lock the door")
            print(f"Moves: {next(self.counter)}")
            escape_key = input("Do you want to enter the key (E/Enter) or find the key (F/Find) ?: ")
            escape_key = escape_key.upper()
            if escape_key in ["E", "ENTER"]:
                self.escape_door(player_data)
            elif escape_key in ["F", "Find"]:
                self.deadly_dining_hall(player_data)
            else:
                print("Invalid key entered. Please enter valid key in order to escape.")
                self.haunted_hallway(player_data)
        elif choice in ["S", "SOUTH"]:
            print(f"Moves: {next(self.counter)}")
            self.deadly_dining_hall(player_data)
        elif choice in ["W", "WEST", "E", "EAST"]:
            print(f"Moves: {next(self.counter)}")
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress(player_data, "haunted_hallway")
        else:
            print("I did not understand that. Let's try again. ")
            print(f"Moves: {next(self.counter)}")
            self.haunted_hallway(player_data)

    def chilling_corridor(self, player_data):
        print("You are in a corridor which is freezing cold.")
        print("You see directions to the north (N) and west (W).")
        print("BEWARE!!! DO NOT go to East (E) or South (S) if you wish not to die the most painful death.")
        print("Remember you can type Save/save the game at any point.")
        print()
        choice = input("Which way will you go to?  Make your choice: ")
        choice = choice.upper()
        if choice in ["N", "North"]:
            print(f"Moves: {next(self.counter)}")
            self.deadly_dining_hall(player_data)
        elif choice in ["W", "WEST"]:
            print(f"Moves: {next(self.counter)}")
            self.spooky_lab(player_data)
        elif choice in ["E", "EAST", "S", "SOUTH"]:
            print(f"Moves: {next(self.counter)}")
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress(player_data, "chilling_corridor")
        else:
            print("I did not understand that. Let's try again. ")
            print(f"Moves: {next(self.counter)}")
            self.chilling_corridor(player_data)

    def sinister_stairway(self, player_data):
        print()
        print("This is a wooden stairway. Be careful!!!")
        print("You see heavy wooden doors at the bottom of the stairs and back to the west.")
        print("BEWARE!!! DO NOT go to East (E) or North (N) if you wish not to die the most painful death.")
        print("Remember you can type Save/save the game at any point.")
        print()
        choice = input("Will you take the door at the bottom of the stairs (S) or back to the west (W)? ")
        choice = choice.upper()
        if choice in ["S", "SOUTH"]:
            print(f"Moves: {next(self.counter)}")
            self.dark_dungeon(player_data)
        elif choice in ["W", "WEST"]:
            print(f"Moves: {next(self.counter)}")
            self.deadly_dining_hall(player_data)
        elif choice in ["N", "NORTH", "E", "EAST"]:
            print(f"Moves: {next(self.counter)}")
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress(player_data, "sinister_stairway")
        else:
            print("I did not understand that. Let's try again. ")
            print(f"Moves: {next(self.counter)}")
            self.sinister_stairway(player_data)

    def spooky_lab(self, player_data):
        print()
        print("You're in a spooky lab with bubbling tubes of phosphorous liquids.")
        print("There's also a monstrous figure in the far corner.  It hasn't seen you yet.")
        print("NOTE: You cannot save the game at this point of time. You have to get our of the spooky lab first.")
        input("Press ENTER to continue.\n")

        print("There's a table with a drawer.\n")
        print("You open the drawer and find instructions on how to get out of the front door.")
        print('The instructions say "There is a keypad on the front door.  To get out, ... ')
        print('Enter the name of what you saw in the Dark Dungeon".\n')
        instructions = ""
        while instructions not in ("Yes", "YES", "yes"):
            instructions = input("Confirm (Yes) that you have read the instructions: ")

        print("\nWell done " + player_data['name'] + ", you're doing great.")
        input("Press ENTER to leave the room.\n")
        print(f"Moves: {next(self.counter)}")
        self.chilling_corridor(player_data)

    def dark_dungeon(self, player_data):
        item_list = ["skeletons", "skulls", "bones", "blood"]
        pick_item = random.choice(item_list)
        key_generator = random.randrange(10000, 1000000)
        self.key_to_escape = pick_item + str(key_generator)
        print(f"You've found a dungeon which has {self.key_to_escape} allover")
        print("Remember what you've seen. This will help you to get out of the house.")
        print("NOTE: You cannot save the game at this point of time. You have to get our of the dark dungeon first.")
        input("Press ENTER to head back up the stairs to the main hall.\n")
        print(f"Moves: {next(self.counter)}")
        self.deadly_dining_hall(player_data)

    def escape_door(self, player_data):
        key_code = ""
        try:
            while key_code != self.key_to_escape:
                key_input = input("Enter the key: ")
                if key_input == self.key_to_escape:
                    print("Lucky. You came out alive!!!")
                    print("Congratulations ! You have finished the HOUSE OF THE DEAD.")
                    self.save_progress(player_data, "escape_door")
                    sys.exit(0)
                else:
                    print("The key you entered is incorrect. Enter valid key")
                    print("NOTE: You cannot save the game at this point of time. "
                          "You have to enter the key or make a decision to back to dining hall first.")
                    look_for_key = input("Enter F or Find to look for key again: ")
                    look_for_key = look_for_key.upper()
                    if look_for_key in ["F", "FIND"]:
                        print(f"Moves: {next(self.counter)}")
                        self.deadly_dining_hall(player_data)
                    else:
                        self.escape_door(player_data)
        except AttributeError:
            print("Seems like you have not obtained the key yet. Please find the key first.")
            print("NOTE: You cannot save the game at this point of time. You have to go back to the dining hall first.")
            print(f"Moves: {next(self.counter)}")
            self.deadly_dining_hall(player_data)


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
