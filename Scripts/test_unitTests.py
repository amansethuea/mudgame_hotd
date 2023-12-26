import unittest
from slow_print import SlowPrint
import re


class CreateTest (unittest.TestCase):

    def setUp (self):
        self.slow_print = SlowPrint()
       

        file = open(self.slow_print.check_dir_file_exists("Resources", "current_game_progress_info.txt"),"r")
        lines = file.readlines()
        lastLineStr=lines[-1]

        self.progressList=(lastLineStr.split(","))

        file2=open(self.slow_print.check_dir_file_exists("Resources", "final_leaderboard.txt"),"r")
        lines2=file2.readlines()
        self.moves=[]
        for i in range(0,len(lines2)):
            lineWords=re.split(r'\s+',lines2[i])
            self.moves.append(lineWords[4])

        file3=open(self.slow_print.check_dir_file_exists("Resources", "level.txt"),"r")
        lines3=file3.readlines()
        self.userIds=[]
        for j in range(0,len(lines3)):
            userIdInLevelTxt=lines3[j].split(',')
            self.userIds.append(userIdInLevelTxt[0])
        

        file4=open(self.slow_print.check_dir_file_exists("Resources", "player_info.txt"),"r")
        lines4=file4.readlines()
        self.userIds2=[]
        for j in range(0,len(lines4)):
            userIdInplayerTxt=lines4[j].split(',')
            self.userIds2.append(userIdInplayerTxt[2])
       
        
class testAge(CreateTest):
    def test_isAgeNumeric(self):
        self.assertTrue(self.progressList[2].isdigit())
        
class testName(CreateTest):
    def test_isNameAlphabetic(self):
        self.assertTrue(self.progressList[0].isalpha())

class testUserId(CreateTest):
    def test_isUserId_No_lessThan_Three_char(self):
        self.assertTrue(len(self.progressList[1])>=3)
    
    def test_isUserId_No_moreThan_Three_char(self):
        self.assertTrue(len(self.progressList[1])<=15)

class testGameStatus(CreateTest):
    def test_isStatusTwhileGameIsNotFinished(self):
        self.location=self.progressList[5]
        if self.location=="escape_door":
            self.assertEqual(self.progressList[7],"T\n")
        else:
            self.assertEqual(self.progressList[7],"F\n")

class testLeaderBoard(CreateTest):
    def test_Is_leaderBoard_well_sorted(self):
        if (len(self.moves)==1 and self.moves[0]=='Moves') or (len(self.moves)==2 and self.moves[0]=='Moves'):
            self.assertEqual(1,1)
        else:
            WellSorted=True
            for index in range(2,len(self.moves)):
                if int(self.moves[index])<int(self.moves[index-1]):
                    WellSorted=False
                    self.assertTrue(WellSorted)
                    return
                else:
                    continue
            self.assertTrue(WellSorted)

class testLevel_and_PlayerInfo(CreateTest):
    def test_levelTxt(self):
        self.assertTrue(self.progressList[1] not in self.userIds)
        
    def test_playerInfoTxt(self):
        self.assertTrue(self.progressList[1] not in self.userIds2)

if __name__ == "__main__":
    o=CreateTest()
    o.setUp()
