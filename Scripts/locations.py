import random
import sys
import re
import csv
from itertools import count
from saving_loading import SaveLoadProcess


class Locations(object):
    def __init__(self, counter):
        self.counter = count(counter)
        self.save_progress = SaveLoadProcess()

    def difficulty_level_handling(self, player_data, counter):
        beginner_max_moves = 101
        intermediate_max_moves = 13
        expert_max_moves = 7

        counter = str(counter)
        count_list = re.findall(r'\b\d+\b', counter)
        move_count = count_list[0]
        move_count = int(move_count)

        with open('../Resources/level.txt', 'r') as data:
            for line in csv.DictReader(data):
                for attr, val in line.items():
                    if attr == 'UserID':
                        if player_data['user_id'] == val:
                            self.difficulty_level = line['Level']
                        else:
                            print(f"{val} not found in level.txt")
                            sys.exit(0)
            data.close()

        if self.difficulty_level in ["expert", "Expert", "EXPERT"] and move_count > expert_max_moves:
            print(f"Hard luck!! You have exhausted the max number of moves at {self.difficulty_level} "
                  f"level i.e 6.")
            print("Please try again. Best of luck!!")
            self.save_progress.make_username_available()
            self.save_progress.clear_user_level_info()
            sys.exit(0)
        elif (self.difficulty_level in ["intermediate", "Intermediate", "INTERMEDIATE"]
              and move_count > intermediate_max_moves):
            print(f"Hard luck!! You have exhausted the max number of moves at {self.difficulty_level} level "
                  f"i.e 12.")
            print("Please try again. Best of luck!!")
            self.save_progress.make_username_available()
            self.save_progress.clear_user_level_info()
            sys.exit(0)
        elif self.difficulty_level in ["beginner", "Beginner", "BEGINNER"] and move_count > beginner_max_moves:
            print(f"Hard luck!! You have exhausted the max number of moves at {self.difficulty_level} "
                  f"level i.e 100.")
            print("Please try again. Best of luck!!")
            self.save_progress.make_username_available()
            self.save_progress.clear_user_level_info()
            sys.exit(0)
        else:
            pass

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
            self.difficulty_level_handling(player_data, self.counter)
            self.haunted_hallway(player_data)
        elif choice in ["S", "SOUTH"]:
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.chilling_corridor(player_data)
        elif choice in ["E", "EAST"]:
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.sinister_stairway(player_data)
        elif choice in ["W", "WEST"]:
            print(f"Moves: {next(self.counter)}")
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "deadly_dining_hall", self.counter)
        else:
            print("I did not understand that. Let's try again. HURRY! You have to get out now!!")
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
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
            if escape_key in ["E", "ENTER", "enter", "Enter"]:
                self.escape_door(player_data)
            elif escape_key in ["F", "Find", "FIND", "find"]:
                self.deadly_dining_hall(player_data)
            else:
                print("Invalid key entered. Please enter valid key in order to escape.")
                self.haunted_hallway(player_data)
        elif choice in ["S", "SOUTH"]:
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.deadly_dining_hall(player_data)
        elif choice in ["W", "WEST", "E", "EAST"]:
            print(f"Moves: {next(self.counter)}")
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "haunted_hallway", self.counter)
        else:
            print("I did not understand that. Let's try again. ")
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
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
            self.difficulty_level_handling(player_data, self.counter)
            self.deadly_dining_hall(player_data)
        elif choice in ["W", "WEST"]:
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.spooky_lab(player_data)
        elif choice in ["E", "EAST", "S", "SOUTH"]:
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "chilling_corridor", self.counter)
        else:
            print("I did not understand that. Let's try again. ")
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
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
            self.difficulty_level_handling(player_data, self.counter)
            self.dark_dungeon(player_data)
        elif choice in ["W", "WEST"]:
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.deadly_dining_hall(player_data)
        elif choice in ["N", "NORTH", "E", "EAST"]:
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
            self.dead(player_data)
        elif choice in ["SAVE"]:
            self.save_progress.save_progress(player_data, "sinister_stairway", self.counter)
        else:
            print("I did not understand that. Let's try again. ")
            print(f"Moves: {next(self.counter)}")
            self.difficulty_level_handling(player_data, self.counter)
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
        self.difficulty_level_handling(player_data, self.counter)
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
        self.difficulty_level_handling(player_data, self.counter)
        self.deadly_dining_hall(player_data)

    def escape_door(self, player_data):
        try:
            key_code = ""
            while key_code != self.key_to_escape:
                key_input = input("Enter the key: ")
                if key_input == self.key_to_escape:
                    print("Lucky. You came out alive!!!")
                    print("Congratulations ! You have finished the HOUSE OF THE DEAD.")
                    self.save_progress.save_progress(player_data, "escape_door", self.counter)
                    sys.exit(0)
                else:
                    print("The key you entered is incorrect. Enter valid key")
                    print("NOTE: You cannot save the game at this point of time. "
                          "You have to enter the key or make a decision to back to dining hall first.")
                    look_for_key = input("Enter F or Find to look for key again: ")
                    look_for_key = look_for_key.upper()
                    if look_for_key in ["F", "FIND"]:
                        print(f"Moves: {next(self.counter)}")
                        self.difficulty_level_handling(player_data, self.counter)
                        self.deadly_dining_hall(player_data)
                    else:
                        self.escape_door(player_data)
        except AttributeError or KeyError:
            print("You have not collected the key to escape. Landing you back to the Deadly Dining Hall")
            self.deadly_dining_hall(player_data)

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
            self.save_progress.save_progress(player_data, "heaven", self.counter)
            sys.exit(0)


if __name__ == "__main__":
    obj = Locations(1)
