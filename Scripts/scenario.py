import os
import unittest
from game_logo import GameLogo
from new_game import NewGame
from slow_print import SlowPrint
from HtmlTestRunner import HTMLTestRunner
from test_unitTests import TestUserId, TestAge, TestName, TestGameStatus, TestLeaderBoard, TestLevelAndPlayerInfo
from pygame import mixer


class HouseOfTheDead(object):
    def __init__(self):
        self.logo = GameLogo()
        self.new_game = NewGame()
        self.slow_print = SlowPrint()

    def main(self):
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "horror-ambience.wav"))
        mixer.music.play()
        print()
        self.logo.logo()
        scenario = ("""
           SCENARIO :-
           It's Halloween night and you happen to discover an abandoned house. 
           You thought it to be a fun haunted house but it turns out to be a real haunted house with zombies and 
           spirits. You need to find the way out of the house as soon as possible !!!! 
           But you are completely unaware about the dangers that lay ahead. I'm the voice in your head  and will guide 
           you throughout. However, remember, one silly move and you are DEAD!!!
        """)
        print(f"\033[1;36;40m\033")
        self.slow_print.print_slow(scenario)
        print('\033[39m')
        self.new_game.start_game()


if __name__ == "__main__":
    obj = HouseOfTheDead()
    obj.main()

    loader = unittest.TestLoader()
    
    suite = (loader.loadTestsFromTestCase(TestAge))
    suite2 = (loader.loadTestsFromTestCase(TestName))
    suite3 = (loader.loadTestsFromTestCase(TestUserId))
    suite4 = (loader.loadTestsFromTestCase(TestGameStatus))
    suite5 = (loader.loadTestsFromTestCase(TestLeaderBoard))
    suite6 = (loader.loadTestsFromTestCase(TestLevelAndPlayerInfo))
    mergedTests = unittest.TestSuite([suite, suite2, suite3, suite4, suite5, suite6])

    if os.path.isdir("../../mudgame_hotd/Tests"):
        dir_name = "../../mudgame_hotd/Tests"
    else:
        dir_name = "../mudgame_hotd/Tests"

    with open(f'{dir_name}/test_report.html', 'w') as f:
     
        runner = HTMLTestRunner(stream=f, combine_reports=True, open_in_browser=True, output=dir_name)
        result = runner.run(mergedTests)
