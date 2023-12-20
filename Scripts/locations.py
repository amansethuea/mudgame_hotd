import random
import sys
import re
import csv
from itertools import count
from saving_loading import SaveLoadProcess
from slow_print import SlowPrint


class Locations(object):
    def __init__(self, counter):
        self.counter = count(counter)
        self.save_progress = SaveLoadProcess()
        self.slow_print = SlowPrint()

    def difficulty_level_handling(self, player_data, counter):
        beginner_max_moves = 101
        intermediate_max_moves = 13
        expert_max_moves = 7

        counter = str(counter)
        count_list = re.findall(r'\b\d+\b', counter)
        move_count = count_list[0]
        move_count = int(move_count)

        with open('../../mudgame_hotd/Resources/level.txt', 'r') as data:
            for line in csv.DictReader(data):
                for attr, val in line.items():
                    if attr == 'UserID':
                        if player_data['user_id'] == val:
                            self.difficulty_level = line['Level']
                        else:
                            self.slow_print.print_slow(f"{val} not found in level.txt")
                            sys.exit(0)
            data.close()

        if self.difficulty_level in ["expert", "Expert", "EXPERT"] and move_count > expert_max_moves:
            self.slow_print.print_slow(f"Hard luck!! You have exhausted the max number of moves at {self.difficulty_level} "
                  f"level i.e 6.")
            self.slow_print.print_slow("Please try again. Best of luck!!")
            self.save_progress.make_username_available()
            self.save_progress.clear_user_level_info()
            sys.exit(0)
        elif (self.difficulty_level in ["intermediate", "Intermediate", "INTERMEDIATE"]
              and move_count > intermediate_max_moves):
            self.slow_print.print_slow(f"Hard luck!! You have exhausted the max number of moves at {self.difficulty_level} level "
                  f"i.e 12.")
            self.slow_print.print_slow("Please try again. Best of luck!!")
            self.save_progress.make_username_available()
            self.save_progress.clear_user_level_info()
            sys.exit(0)
        elif self.difficulty_level in ["beginner", "Beginner", "BEGINNER"] and move_count > beginner_max_moves:
            self.slow_print.print_slow(f"Hard luck!! You have exhausted the max number of moves at {self.difficulty_level} "
                  f"level i.e 100.")
            self.slow_print.print_slow("Please try again. Best of luck!!")
            self.save_progress.make_username_available()
            self.save_progress.clear_user_level_info()
            sys.exit(0)
        else:
            pass

    def deadly_dining_hall(self, player_data):
        print()
        self.slow_print.print_slow("You are in the main dining hall of the haunted house, standing alone, in the dark.")
        self.slow_print.print_slow("You see three ways to go.")
        self.slow_print.print_slow("Do you go to the north (N), south (S) or east (E)?.")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to go the West")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        print()
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
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "deadly_dining_hall", self.counter)
        else:
            self.slow_print.print_slow("I did not understand that. Let's try again. HURRY! You have to get out now!!")
            self.slow_print.print_slow(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.deadly_dining_hall(player_data)

    def haunted_hallway(self, player_data):
        self.slow_print.print_slow("You are in a creepy hallway where zombies are roaming looking for prey to suck blood out of them")
        self.slow_print.print_slow("You notice there are ways to the north (N) and south (S).")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to go the West (W) or East (E) if you don't wish to die the most painful death.")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        print()
        choice = input("Enter either N/North or S/South: ")
        choice = choice.upper()
        if choice in ["N", "NORTH"]:
            print()
            self.slow_print.print_slow("Oh! you have found the escape door. But it's locked")
            self.slow_print.print_slow("There is a key in one of the locations of the house to un-lock the door")
            self.slow_print.print_slow(f"Moves: {next(self.counter)}")
            escape_key = input("Do you want to enter the key (E/Enter) or find the key (F/Find) ?: ")
            escape_key = escape_key.upper()
            if escape_key in ["E", "ENTER", "enter", "Enter"]:
                self.escape_door(player_data)
            elif escape_key in ["F", "Find", "FIND", "find"]:
                self.deadly_dining_hall(player_data)
            else:
                self.slow_print.print_slow("Invalid key entered. Please enter valid key in order to escape.")
                self.haunted_hallway(player_data)
        elif choice in ["S", "SOUTH"]:
            self.slow_print.print_slow(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.deadly_dining_hall(player_data)
        elif choice in ["W", "WEST", "E", "EAST"]:
            self.slow_print.print_slow(f"Moves: {next(self.counter)}")
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "haunted_hallway", self.counter)
        else:
            self.slow_print.print_slow("I did not understand that. Let's try again. ")
            self.slow_print.print_slow(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.haunted_hallway(player_data)

    def chilling_corridor(self, player_data):
        self.slow_print.print_slow("You are in a corridor which is freezing cold.")
        self.slow_print.print_slow("You see directions to the north (N) and west (W).")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to East (E) or South (S) if you wish not to die the most painful death.")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        print()
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
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "chilling_corridor", self.counter)
        else:
            self.slow_print.print_slow("I did not understand that. Let's try again. ")
            self.slow_print.print_slow(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.chilling_corridor(player_data)

    def sinister_stairway(self, player_data):
        print()
        self.slow_print.print_slow("This is a wooden stairway. Be careful!!!")
        self.slow_print.print_slow("You see heavy wooden doors at the bottom of the stairs and back to the west.")
        self.slow_print.print_slow("BEWARE!!! DO NOT go to East (E) or North (N) if you wish not to die the most painful death.")
        self.slow_print.print_slow("Remember you can type Save/save the game at any point.")
        print()
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
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "sinister_stairway", self.counter)
        else:
            self.slow_print.print_slow("I did not understand that. Let's try again. ")
            self.slow_print.print_slow(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.sinister_stairway(player_data)

    def spooky_lab(self, player_data):
        print()
        self.slow_print.print_slow("You're in a spooky lab with bubbling tubes of phosphorous liquids.")
        self.slow_print.print_slow("There's also a monstrous figure in the far corner.  It hasn't seen you yet.")
        self.slow_print.print_slow("NOTE: You cannot save the game at this point of time. You have to get our of the spooky lab first.")
        input("Press ENTER to continue.\n")

        self.slow_print.print_slow("There's a table with a drawer.\n")
        self.slow_print.print_slow("You open the drawer and find instructions on how to get out of the front door.")
        self.slow_print.print_slow('The instructions say "There is a keypad on the front door.  To get out, ... ')
        self.slow_print.print_slow('Enter the name of what you saw in the Dark Dungeon".\n')
        instructions = ""
        while instructions not in ("Yes", "YES", "yes"):
            instructions = input("Confirm (Yes) that you have read the instructions: ")

        self.slow_print.print_slow("\nWell done " + player_data['name'] + ", you're doing great.")
        input("Press ENTER to leave the room.\n")
        self.slow_print.print_slow(f"Moves: {next(self.counter)}")
        self.difficulty_level_handling(player_data, self.counter)
        self.chilling_corridor(player_data)

    def dark_dungeon(self, player_data):
        item_list = ["skeletons", "skulls", "bones", "blood"]
        pick_item = random.choice(item_list)
        key_generator = random.randrange(10000, 1000000)
        self.key_to_escape = pick_item + str(key_generator)
        self.slow_print.print_slow(f"You've found a dungeon which has {self.key_to_escape} allover")
        self.slow_print.print_slow("Remember what you've seen. This will help you to get out of the house.")
        self.slow_print.print_slow("NOTE: You cannot save the game at this point of time. You have to get our of the dark dungeon first.")
        input("Press ENTER to head back up the stairs to the main hall.\n")
        self.slow_print.print_slow(f"Moves: {next(self.counter)}")
        self.difficulty_level_handling(player_data, self.counter)
        self.deadly_dining_hall(player_data)

    def escape_door(self, player_data):
        try:
            key_code = ""
            while key_code != self.key_to_escape:
                key_input = input("Enter the key: ")
                if key_input == self.key_to_escape:
                    self.slow_print.print_slow("Lucky. You came out alive!!!")
                    self.slow_print.print_slow("Congratulations ! You have finished the HOUSE OF THE DEAD.")
                    self.save_progress.save_progress(player_data, "escape_door", self.counter)
                    sys.exit(0)
                else:
                    self.slow_print.print_slow("The key you entered is incorrect. Enter valid key")
                    self.slow_print.print_slow("NOTE: You cannot save the game at this point of time. "
                          "You have to enter the key or make a decision to back to dining hall first.")
                    look_for_key = input("Enter F or Find to look for key again: ")
                    look_for_key = look_for_key.upper()
                    if look_for_key in ["F", "FIND"]:
                        self.slow_print.print_slow(f"Moves: {next(self.counter)}")
                        self.difficulty_level_handling(player_data, self.counter)
                        self.deadly_dining_hall(player_data)
                    else:
                        self.escape_door(player_data)
        except AttributeError or KeyError:
            print("You have not collected the key to escape. Landing you back to the Deadly Dining Hall")
            self.deadly_dining_hall(player_data)

    def dead(self, player_data):
        self.slow_print.print_slow("\nYou push some unwanted door, it creeks as it opens.")
        self.slow_print.print_slow("This is a very strange, dark place, but you walk in.")
        self.slow_print.print_slow("The door slams shut !!\n")
        self.slow_print.print_slow("ZOMBIES !!!\n")
        self.slow_print.print_slow("You're ...DEAD !!\n")
        self.slow_print.print_slow("I warned you not go that way.")
        self.slow_print.print_slow(f"Oh dear {player_data['name']}. Never mind. Do you wish to play again?")
        play_again = input('Type "YES" (and press ENTER) to play again, or just press ENTER to end the program. \n')
        if play_again in ["YES", "yes", "Yes"]:
            self.deadly_dining_hall(player_data)
        else:
            self.slow_print.print_slow("Thank you for playing the HOTD. See you next time!")
            self.save_progress.save_progress(player_data, "heaven", self.counter)
            sys.exit(0)


if __name__ == "__main__":
    obj = Locations(1)
