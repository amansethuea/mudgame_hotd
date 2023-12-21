import unittest
from slow_print import SlowPrint


class CreateTest (unittest.TestCase):

    def setUp (self):
        self.slow_print = SlowPrint()
        file = open(self.slow_print.check_dir_file_exists("Resources", "current_game_progress_info.txt"),"r")
        lines = file.readlines()
        lastLineStr=lines[-1]

        self.progressList=(lastLineStr.split(","))
        print(self.progressList)
        print(self.progressList[2].isdigit())

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

        
