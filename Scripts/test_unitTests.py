import unittest
from slow_print import SlowPrint
import re


class CreateTest(unittest.TestCase):

    def setUp(self):
        self.slow_print = SlowPrint()

        file = open(self.slow_print.check_dir_file_exists("Resources",
                                                          "current_game_progress_info.txt"), "r")
        lines = file.readlines()
        last_line_str = lines[-1]

        self.progressList = (last_line_str.split(","))

        file2 = open(self.slow_print.check_dir_file_exists("Resources", "final_leaderboard.txt"), "r")
        lines2 = file2.readlines()
        self.moves = []
        for i in range(0, len(lines2)):
            line_words = re.split(r'\s+', lines2[i])
            self.moves.append(line_words[4])

        file3 = open(self.slow_print.check_dir_file_exists("Resources", "level.txt"), "r")
        lines3 = file3.readlines()
        self.userIds = []
        for j in range(0, len(lines3)):
            user_id_in_level_txt = lines3[j].split(',')
            if len(user_id_in_level_txt) == 1:
                continue
            self.userIds.append(user_id_in_level_txt[0])

        file_4 = open(self.slow_print.check_dir_file_exists("Resources", "player_info.txt"), "r")
        lines_4 = file_4.readlines()
        self.userIds2 = []
        for j in range(0, len(lines_4)):
            user_id_in_player_txt = lines_4[j].split(',')
            if len(user_id_in_player_txt) == 1:
                continue
            self.userIds2.append(user_id_in_player_txt[2])


class TestAge(CreateTest):
    def test_is_age_numeric(self):
        self.assertTrue(self.progressList[2].isdigit())


class TestName(CreateTest):
    def test_is_name_alphabetic(self):
        self.assertTrue(self.progressList[0].isalpha())


class TestUserId(CreateTest):
    def test_isUserId_No_lessThan_Three_char(self):
        self.assertTrue(len(self.progressList[1]) >= 3)

    def test_is_user_id_no_more_than_three_char(self):
        self.assertTrue(len(self.progressList[1]) <= 15)


class TestGameStatus(CreateTest):
    def test_is_status_t_while_game_is_not_finished(self):
        self.location = self.progressList[5]
        if self.location == "escape_door":
            self.assertEqual(self.progressList[7], "T\n")
        else:
            self.assertEqual(self.progressList[7], "F\n")


class TestLeaderBoard(CreateTest):
    def test_Is_leaderBoard_well_sorted(self):
        if (len(self.moves) == 1 and self.moves[0] == 'Moves') or (len(self.moves) == 2 and self.moves[0] == 'Moves'):
            self.assertEqual(1, 1)
        else:
            well_sorted = True
            for index in range(2, len(self.moves)):
                if int(self.moves[index]) < int(self.moves[index - 1]):
                    well_sorted = False
                    self.assertTrue(well_sorted)
                    return
                else:
                    continue
            self.assertTrue(well_sorted)


class TestLevelAndPlayerInfo(CreateTest):
    def test_level_txt(self):
        self.location = self.progressList[5]
        if self.location == "heaven" or self.location == "escape_door":
            self.assertTrue(self.progressList[1] not in self.userIds)

    def test_player_info_txt(self):
        self.location = self.progressList[5]
        if self.location == "heaven" or self.location == "escape_door":
            self.assertTrue(self.progressList[1] not in self.userIds2)


if __name__ == "__main__":
    o = CreateTest()
    o.setUp()
