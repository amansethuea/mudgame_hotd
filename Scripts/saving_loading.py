import csv
import re
import sys
import time
import progressbar
from datetime import datetime
import pandas as pandasForSortingCSV


class SaveLoadProcess(object):
    def make_username_available(self):
        f = open("../Resources/player_info.txt", "w")
        f.write("")
        f.write("Name,Age,UserID,Character")
        f.close()

    def sort_leaderboard(self):
        with open("../Resources/leaderboard.txt", 'r') as r:
            next(r)
            rr = csv.reader(r)
            f = open("../Resources/final_leaderboard.txt", "w")
            f.write("Name,UserID,Character,Moves,Date&Time\n")
            for row in rr:
                get_count = row[3]
                count_list = re.findall(r'\b\d+\b', get_count)
                count = count_list[0]
                count = int(count)
                f.write(row[0] + "," + row[1] + "," + row[2] + "," + str(count) + "," + row[4] + "\n")
            f.close()
            r.close()

        csvData = pandasForSortingCSV.read_csv("../Resources/final_leaderboard.txt")
        csvData.sort_values(["Moves"],
                            axis=0,
                            ascending=[True],
                            inplace=True)
        fo = open("../Resources/final_leaderboard.txt", "w")
        fo.write("")
        fo.write(str(csvData))
        fo.close()

    def leaderboard(self, player_data, move_counter):
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('../Resources/leaderboard.txt', 'a', newline='\n') as csvfile:
            write_current_progress = csv.writer(csvfile, delimiter=',')
            if self.check_header_existence('../Resources/leaderboard.txt'):
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 move_counter, date_time])
            else:
                write_current_progress.writerow(["Name", "UserID", "Character", "Moves", "Date&Time"])
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 move_counter, date_time])
            csvfile.close()

    def check_header_existence(self, file_name):
        fo = open(file_name, 'r')
        data = fo.readlines()
        for lines in data:
            lines = lines.split(",")
            if lines[0] == "Name":
                return True
            else:
                return False

    def progress_bar(self):
        loop_count = 100
        with progressbar.ProgressBar(max_value=loop_count) as bar:
            for i in range(loop_count):
                bar.update(i)
                time.sleep(0.01)

    def save_progress(self, player_data, location, move_counter):
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('../Resources/current_game_progress_info.txt', 'a', newline='\n') as csvfile:
            write_current_progress = csv.writer(csvfile, delimiter=',')
            if location in ["escape_door"]:
                game_completion = "T"
                self.leaderboard(player_data, move_counter)
                self.sort_leaderboard()
                self.make_username_available()
            else:
                game_completion = "F"
            if self.check_header_existence('../Resources/current_game_progress_info.txt'):
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 move_counter, location, date_time, game_completion])
            else:
                write_current_progress.writerow(["Name", "UserID", "Character", "Moves", "CurrentLocation", "Date&Time",
                                                 "GameCompletion"])
                write_current_progress.writerow([player_data['name'], player_data['user_id'], player_data['char'],
                                                 move_counter, location, date_time, game_completion])
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
        get_user_dict, game_version_list = {}, []
        with open('../Resources/current_game_progress_info.txt', 'r') as data:
            for line in csv.DictReader(data):
                for attr, val in line.items():
                    if attr == 'UserID':
                        if user_id == val:
                            game_version_list.append(line)
            data.close()

        fetch_latest_progress = game_version_list[-1]
        get_user_dict = fetch_latest_progress

        if get_user_dict:
            # Forming player_data dict. Giving a random age as age is not used anywhere other than player_info.txt
            player_data = {"name": get_user_dict["Name"], "age": 20, "user_id": get_user_dict["UserID"],
                           "char": get_user_dict["Character"]}
            print(f"Please wait. Loading game for user {get_user_dict['UserID']}")
            self.progress_bar()
            from locations import Locations
            if get_user_dict['CurrentLocation'] == 'deadly_dining_hall':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                locations = Locations(get_move_count)
                locations.deadly_dining_hall(player_data)
            elif get_user_dict['CurrentLocation'] == 'haunted_hallway':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                locations = Locations(get_move_count)
                locations.haunted_hallway(player_data)
            elif get_user_dict['CurrentLocation'] == 'chilling_corridor':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                locations = Locations(get_move_count)
                locations.chilling_corridor(player_data)
            elif get_user_dict['CurrentLocation'] == 'sinister_stairway':
                get_move_count = self.get_move_counter_for_load_game(get_user_dict['Moves'])
                locations = Locations(get_move_count)
                locations.sinister_stairway(player_data)
            elif get_user_dict['CurrentLocation'] == "escape_door":
                print("You have already finished the game. Please start a new game.")
                sys.exit(0)
            else:
                print("Invalid Location")
        else:
            print(f"{user_id} user not found. Please start a new game.")


if __name__ == "__main__":
    obj = SaveLoadProcess()