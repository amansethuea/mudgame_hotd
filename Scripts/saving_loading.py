import csv
import re
import time
import progressbar
from datetime import datetime


class SaveLoadProcess(object):
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
        get_user_dict = {}
        with open('../Resources/current_game_progress_info.txt', 'r') as data:
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
            else:
                print("Invalid Location")
        else:
            print(f"{user_id} user not found. Please start a new game.")


if __name__ == "__main__":
    obj = SaveLoadProcess()