import random
import re
import csv
import sys

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from itertools import count
from saving_loading import SaveLoadProcess
from slow_print import SlowPrint
from challenges import Challenges
from pygame import mixer


class Locations(object):
    def __init__(self, counter):
        self.counter = count(counter)
        self.save_progress = SaveLoadProcess()
        self.slow_print = SlowPrint()
        self.challenge = Challenges()
        self.spooky_lab_challenge_completion = False
        self.escape_door_challenge_completion = False

    def difficulty_level_handling(self, player_data, counter):
        beginner_max_moves = 101
        intermediate_max_moves = 13
        expert_max_moves = 7

        counter = str(counter)
        count_list = re.findall(r'\b\d+\b', counter)
        move_count = count_list[0]
        move_count = int(move_count)
        get_file = self.slow_print.check_dir_file_exists("Resources", "level.txt")
        with open(get_file, 'r') as data:
            for line in csv.DictReader(data):
                for attr, val in line.items():
                    if attr == 'UserID':
                        if player_data['user_id'] == val:
                            self.difficulty_level = line['Level']
            data.close()

        if self.difficulty_level in ["expert", "Expert", "EXPERT"] and move_count > expert_max_moves:
            self.slow_print.print_slow(f"Hard luck!! You have exhausted the max number of moves "
                                       f"at {self.difficulty_level} level i.e 6.")
            self.slow_print.print_slow("Please try again. Best of luck!!")
            self.save_progress.save_progress(player_data, "heaven", "count("+str(expert_max_moves)+")")
            sys.exit(0)
        elif (self.difficulty_level in ["intermediate", "Intermediate", "INTERMEDIATE"]
              and move_count > intermediate_max_moves):
            self.slow_print.print_slow(f"Hard luck!! You have exhausted the max number of moves "
                                       f"at {self.difficulty_level} level i.e 12.")
            self.slow_print.print_slow("Please try again. Best of luck!!")
            self.save_progress.save_progress(player_data, "heaven", "count("+str(intermediate_max_moves)+")")
            sys.exit(0)
        elif self.difficulty_level in ["beginner", "Beginner", "BEGINNER"] and move_count > beginner_max_moves:
            self.slow_print.print_slow(f"Hard luck!! You have exhausted the max number of "
                                       f"moves at {self.difficulty_level} level i.e 100.")
            self.slow_print.print_slow("Please try again. Best of luck!!")
            self.save_progress.save_progress(player_data, "heaven", "count("+str(beginner_max_moves)+")")
            sys.exit(0)
        else:
            pass

    def deadly_dining_hall(self, player_data):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "horror-ambience.wav"))
        mixer.music.play()
        print(f"\033[1;36;40m\033")
        print()
        self.slow_print.print_slow("You are in the main dining hall of the haunted house, standing alone, in the dark.")
        self.slow_print.print_slow("You see three ways to go.")
        self.slow_print.print_slow("Do you go to the north (N), south (S) or east (E)?.")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to go the West")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        self.slow_print.print_slow("Type Help / Map / Show Map to get current information")
        print()
        print('\033[39m')

        def sub_function_dining_hall():
            choice = input("Enter either N/North, S/South or E/East: ")
            choice = choice.upper()
            if choice in ["N", "NORTH"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.haunted_hallway(player_data)
            elif choice in ["S", "SOUTH"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.chilling_corridor(player_data)
            elif choice in ["E", "EAST"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.sinister_stairway(player_data)
            elif choice in ["W", "WEST"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.dead(player_data)
            elif choice in ["MAP", "SHOW MAP", "HELP"]:
                get_img = self.slow_print.check_dir_file_exists("Resources/Images",
                                                                "location_full_map.png")
                img = mpimg.imread(get_img)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                sub_function_dining_hall()
            elif choice in ["SAVE"]:
                self.save_progress.save_progress(player_data, "deadly_dining_hall", self.counter)
                print(f"\033[1;38;40m\033")
                self.slow_print.print_slow("Do you wish to continue playing or exit ?")
                print('\033[39m')
                while True:
                    print(f"\033[1;38;40m\033")
                    enter_choice = input("Please choose either C (Continue) or E (Exit): ")
                    if enter_choice.upper() in ["E", "EXIT"]:
                        self.slow_print.print_slow("Exiting. See you soon!!")
                        return
                    elif enter_choice.upper() in ["C", "CONT", "CONTINUE"]:
                        self.slow_print.print_slow("Continuing game after save")
                        sub_function_dining_hall()
                        break
                    else:
                        self.slow_print.print_slow("Invalid input. Please choose either C or E.")
                    print('\033[39m')
            else:
                print(f"\033[1;38;40m\033")
                self.slow_print.print_slow(
                    "I did not understand that. Let's try again. HURRY! You have to get out now!!")
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                print('\033[39m')
                self.deadly_dining_hall(player_data)
        sub_function_dining_hall()

    def haunted_hallway(self, player_data):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "horror-ambience.wav"))
        mixer.music.play()
        print(f"\033[1;37;40m\033")
        self.slow_print.print_slow("You are in a creepy hallway where zombies are roaming looking for prey to suck "
                                   "blood out of them")
        self.slow_print.print_slow("You notice there are ways to the north (N) and south (S).")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to go the West (W) or East (E) if you don't wish to die "
                                   "the most painful death.")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        self.slow_print.print_slow("Type Help / Map / Show Map to get current information")
        print()
        print('\033[39m')

        def sub_function_haunted_hallway():
            choice = input("Enter either N/North or S/South: ")
            choice = choice.upper()
            if choice in ["N", "NORTH"]:
                print()
                self.slow_print.print_slow("Oh! you have found the escape door. But it's locked")
                self.slow_print.print_slow("There is a key in one of the locations of the house to un-lock the door")
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                while True:
                    escape_key = input("Do you want to enter the key (E/Enter) or find the key (F/Find) ?: ")
                    escape_key = escape_key.upper()
                    if escape_key in ["E", "ENTER", "enter", "Enter"]:
                        self.escape_door(player_data)
                        break
                    elif escape_key in ["F", "Find", "FIND", "find"]:
                        self.deadly_dining_hall(player_data)
                        break
                    else:
                        self.slow_print.print_slow("Invalid input given. Please enter either E/Enter or F/Find")
            elif choice in ["S", "SOUTH"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.deadly_dining_hall(player_data)
            elif choice in ["W", "WEST", "E", "EAST"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.dead(player_data)
            elif choice in ["MAP", "SHOW MAP", "HELP"]:
                get_img = self.slow_print.check_dir_file_exists("Resources/Images",
                                                                "location_full_map.png")
                img = mpimg.imread(get_img)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                sub_function_haunted_hallway()
            elif choice in ["SAVE"]:
                self.save_progress.save_progress(player_data, "haunted_hallway", self.counter)
                self.slow_print.print_slow("Do you wish to continue playing or exit ?")
                while True:
                    enter_choice = input("Please choose either C (Continue) or E (Exit): ")
                    if enter_choice.upper() in ["E", "EXIT"]:
                        self.slow_print.print_slow("Exiting. See you soon!!")
                        return
                    elif enter_choice.upper() in ["C", "CONT", "CONTINUE"]:
                        self.slow_print.print_slow("Continuing game after save")
                        sub_function_haunted_hallway()
                        break
                    else:
                        self.slow_print.print_slow("Invalid input. Please choose either C or E.")
            else:
                self.slow_print.print_slow("I did not understand that. Let's try again. ")
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.haunted_hallway(player_data)
        sub_function_haunted_hallway()

    def chilling_corridor(self, player_data):
        print(f"\033[1;35;40m\033")
        print()
        self.slow_print.print_slow("You are in a corridor which is freezing cold.")
        self.slow_print.print_slow("You see directions to the north (N) and west (W).")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to East (E) or South (S) if you wish not to die the most "
                                   "painful death.")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        self.slow_print.print_slow("Type Help / Map / Show Map to get current information")
        print()
        print('\033[39m')

        def sub_function_chilling_corridor():
            choice = input("Which way will you go to?  Make your choice: ")
            choice = choice.upper()
            if choice in ["N", "North"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.deadly_dining_hall(player_data)
            elif choice in ["W", "WEST"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.spooky_lab(player_data)
            elif choice in ["E", "EAST", "S", "SOUTH"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.dead(player_data)
            elif choice in ["MAP", "SHOW MAP", "HELP"]:
                get_img = self.slow_print.check_dir_file_exists("Resources/Images",
                                                                "location_full_map.png")
                img = mpimg.imread(get_img)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                sub_function_chilling_corridor()
            elif choice in ["SAVE"]:
                self.save_progress.save_progress(player_data, "chilling_corridor", self.counter)
                self.slow_print.print_slow("Do you wish to continue playing or exit ?")
                while True:
                    enter_choice = input("Please choose either C (Continue) or E (Exit): ")
                    if enter_choice.upper() in ["E", "EXIT"]:
                        self.slow_print.print_slow("Exiting. See you soon!!")
                        return
                    elif enter_choice.upper() in ["C", "CONT", "CONTINUE"]:
                        self.slow_print.print_slow("Continuing game after save")
                        sub_function_chilling_corridor()
                        break
                    else:
                        self.slow_print.print_slow("Invalid input. Please choose either C or E.")
            else:
                self.slow_print.print_slow("I did not understand that. Let's try again. ")
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.chilling_corridor(player_data)
        sub_function_chilling_corridor()

    def sinister_stairway(self, player_data):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "horror-ambience.wav"))
        mixer.music.play()
        print(f"\033[1;34;40m\033")
        print()
        self.slow_print.print_slow("This is a wooden stairway. Be careful!!!")
        self.slow_print.print_slow("You see heavy wooden doors at the bottom of the stairs and back to the west.")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to East (E) or North (N) if you wish not to die the most "
                                   "painful death.")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        self.slow_print.print_slow("Type Help / Map / Show Map to get current information")
        print()
        print('\033[39m')

        def sub_function_sinister_stairway():
            choice = input("Will you take the door at the bottom of the stairs (S) or back to the west (W)? ")
            choice = choice.upper()
            if choice in ["S", "SOUTH"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.dark_dungeon(player_data)
            elif choice in ["W", "WEST"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.deadly_dining_hall(player_data)
            elif choice in ["N", "NORTH", "E", "EAST"]:
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.dead(player_data)
            elif choice in ["MAP", "SHOW MAP", "HELP"]:
                get_img = self.slow_print.check_dir_file_exists("Resources/Images",
                                                                "location_full_map.png")
                img = mpimg.imread(get_img)
                plt.imshow(img)
                plt.axis('off')
                plt.show()
                sub_function_sinister_stairway()
            elif choice in ["SAVE"]:
                self.save_progress.save_progress(player_data, "sinister_stairway", self.counter)
                self.slow_print.print_slow("Do you wish to continue playing or exit ?")
                while True:
                    enter_choice = input("Please choose either C (Continue) or E (Exit): ")
                    if enter_choice.upper() in ["E", "EXIT"]:
                        self.slow_print.print_slow("Exiting. See you soon!!")
                        return
                    elif enter_choice.upper() in ["C", "CONT", "CONTINUE"]:
                        self.slow_print.print_slow("Continuing game after save")
                        sub_function_sinister_stairway()
                        break
                    else:
                        self.slow_print.print_slow("Invalid input. Please choose either C or E.")
            else:
                self.slow_print.print_slow("I did not understand that. Let's try again. ")
                self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                self.difficulty_level_handling(player_data, self.counter)
                self.sinister_stairway(player_data)
        sub_function_sinister_stairway()

    def spooky_lab(self, player_data):
        print(f"\033[1;33;40m\033")
        print()
        self.slow_print.print_slow("You're in a spooky lab with bubbling tubes of phosphorous liquids.")
        self.slow_print.print_slow("There's also a monstrous figure in the far corner.  It hasn't seen you yet.")
        self.slow_print.print_slow("NOTE: You cannot save the game at this point of time. You have to get our of the "
                                   "spooky lab first.")
        input("Press ENTER to continue.\n")

        self.slow_print.print_slow("There's a table with a drawer.\n")
        self.slow_print.print_slow("You open the drawer and find instructions on how to get out of the front door.")
        self.slow_print.print_slow('The instructions say "There is a keypad on the front door.  To get out, ... ')
        self.slow_print.print_slow('Enter the name of what you saw in the Dark Dungeon".\n')
        print('\033[39m')
        instructions = ""
        while instructions not in ("Yes", "YES", "yes"):
            instructions = input("Confirm (Yes) that you have read the instructions: ")

        self.slow_print.print_slow("\nWell done " + player_data['name'] + ", you're doing great.")
        input("Press ENTER to leave the room.\n")
        self.slow_print.print_slow(f"Moves: {next(self.counter)}")
        self.difficulty_level_handling(player_data, self.counter)

        if not self.spooky_lab_challenge_completion:
            lab_challenge = self.challenge.spooky_lab_escape_challenge()
            if lab_challenge:
                self.spooky_lab_challenge_completion = True
                self.slow_print.print_slow("GREAT JOB! You have successfully passed the Spooky Lab escape challenge")
            else:
                self.dead_in_challenge(player_data, "Spooky Lab escape")
                return
        else:
            self.slow_print.print_slow(
                "Seems like you have already completed Spooky Lab escape challenge. Proceeding..")

        self.chilling_corridor(player_data)

    def dark_dungeon(self, player_data):
        item_list = ["skeletons", "skulls", "bones", "blood"]
        pick_item = random.choice(item_list)
        key_generator = random.randrange(10000, 1000000)
        self.key_to_escape = pick_item + str(key_generator)
        print(f"\033[1;32;40m\033")
        self.slow_print.print_slow(f"You've found a dungeon which has {self.key_to_escape} allover")
        self.slow_print.print_slow("Remember what you've seen. This will help you to get out of the house.")
        self.slow_print.print_slow("NOTE: You cannot save the game at this point of time. You have to get our of the "
                                   "dark dungeon first.")
        input("Press ENTER to head back up the stairs to the main hall.\n")
        self.slow_print.print_slow(f"Moves: {next(self.counter)}")
        print('\033[39m')
        self.difficulty_level_handling(player_data, self.counter)
        self.deadly_dining_hall(player_data)

    def escape_door(self, player_data):
        try:
            key_input = input("Enter the key: ")
            if key_input == self.key_to_escape:
                self.slow_print.print_slow("GREAT! The entered key is valid")
                print()
                escape_door_challenge = self.challenge.escape_door_challenge()
                if escape_door_challenge:
                    self.slow_print.print_slow("GREAT JOB! You have successfully passed the Escape Door challenge")
                    self.slow_print.print_slow("Lucky. You came out alive!!!")
                    self.slow_print.print_slow("Congratulations ! You have finished the HOUSE OF THE DEAD.")
                    self.save_progress.save_progress(player_data, "escape_door", self.counter)
                    return
                else:
                    self.dead_in_challenge(player_data, "Escape Door")
                    return
            else:
                self.slow_print.print_slow("The key invalid. The zombie attacked you. You DIED!!")
                self.slow_print.print_slow("GAME OVER!!")
                self.save_progress.save_progress(player_data, "heaven", self.counter)
                return False
        except AttributeError or KeyError:
            self.slow_print.print_slow("ERROR!! You have not collected the key to escape. Landing you back to the "
                                       "Deadly Dining Hall")
            self.deadly_dining_hall(player_data)

    def dead(self, player_data):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "player_dead.wav"))
        mixer.music.play()
        self.slow_print.print_slow("\nYou push some unwanted door, it creeks as it opens.")
        self.slow_print.print_slow("This is a very strange, dark place, but you walk in.")
        self.slow_print.print_slow("The door slams shut !!\n")
        self.slow_print.print_slow("ZOMBIES !!!\n")
        self.slow_print.print_slow("You're ...DEAD !!\n")
        self.slow_print.print_slow("I warned you not go that way.")
        self.slow_print.print_slow(f"Oh dear {player_data['name']}. Never mind. Do you wish to play again?")
        play_again = input('Type "YES" (and press ENTER) to play again, or just press ENTER to end the program: ')
        if play_again in ["YES", "yes", "Yes"]:
            self.deadly_dining_hall(player_data)
        else:
            self.slow_print.print_slow("Thank you for playing the HOTD. See you next time!")
            self.save_progress.save_progress(player_data, "heaven", self.counter)

    def dead_in_challenge(self, player_data, challenge_name):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "player_dead.wav"))
        mixer.music.play()
        self.slow_print.print_slow(f"\n You lost the {challenge_name} challenge")
        self.slow_print.print_slow("You're ...DEAD !!\n")
        self.slow_print.print_slow(f"Oh dear {player_data['name']}. Never mind. Do you wish to play again?")
        play_again = input('Type "YES" (and press ENTER) to play again, or just press ENTER to end the program: ')
        if play_again in ["YES", "yes", "Yes"]:
            self.deadly_dining_hall(player_data)
        else:
            self.slow_print.print_slow("Thank you for playing the HOTD. See you next time!")
            self.save_progress.save_progress(player_data, "heaven", self.counter)


if __name__ == "__main__":
    obj = Locations(1)
