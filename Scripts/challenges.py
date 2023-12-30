from slow_print import SlowPrint
from pygame import mixer


class Challenges(object):
    def __init__(self):
        self.slow_print = SlowPrint()

    def spooky_lab_escape_challenge(self):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "horror-ambience.wav"))
        mixer.music.play()
        print(f"\033[1;35;40m\033")
        print()
        self.slow_print.print_slow("Not so easy to get out of the spooky lab")
        self.slow_print.print_slow("There is vicious zombie at the door of the spooky lab")
        self.slow_print.print_slow("You have to dodge the zombie in order to escape the lab")
        self.slow_print.print_slow("Here is a science quiz challenge ")
        input("Press ENTER to start the challenge")
        print("\n")
        correct_ans_list, wrong_ans_list = [], []
        self.slow_print.print_slow("Q1. What is the chemical formula for water ?")
        self.slow_print.print_slow("A) CO B) CO₂ C) H₂O")
        while True:
            first_ans = input("Enter answer: ")
            if first_ans.upper() == "C":
                self.slow_print.print_slow("FANTASTIC! Correct answer")
                correct_ans_list.append("yes")
                break
            elif first_ans.upper() in ["B", "A"]:
                self.slow_print.print_slow("Oops! Wrong answer")
                wrong_ans_list.append("no")
                break
            else:
                print("Invalid input given. Please enter either A, B or C")

        self.slow_print.print_slow("Q2. What is the chemical formula for Sulphuric Acid ?")
        self.slow_print.print_slow("A) H₂SO₄ B) NO₂  C) HNO₃")
        while True:
            first_ans = input("Enter answer: ")
            if first_ans.upper() == "A":
                self.slow_print.print_slow("FANTASTIC! Correct answer")
                correct_ans_list.append("yes")
                break
            elif first_ans.upper() in ["B", "C"]:
                self.slow_print.print_slow("Oops! Wrong answer")
                wrong_ans_list.append("no")
                break
            else:
                print("Invalid input given. Please enter either A, B or C")

        self.slow_print.print_slow("Q3. What is the chemical formula for Hydrochloric Acid ?")
        self.slow_print.print_slow("A) H₂SO₄ B) HCL  C) HNO₃")
        while True:
            first_ans = input("Enter answer: ")
            if first_ans.upper() == "B":
                self.slow_print.print_slow("FANTASTIC! Correct answer")
                correct_ans_list.append("yes")
                break
            elif first_ans.upper() in ["A", "C"]:
                self.slow_print.print_slow("Oops! Wrong answer")
                wrong_ans_list.append("no")
                break
            else:
                print("Invalid input given. Please enter either A, B or C")

        print('\033[39m')
        if len(correct_ans_list) > len(wrong_ans_list):
            return True
        else:
            return False

    def escape_door_challenge(self):
        mixer.music.stop()
        mixer.init()
        mixer.music.load(self.slow_print.check_dir_file_exists("Resources/Audio",
                                                               "horror-ambience.wav"))
        mixer.music.play()
        print(f"\033[1;34;40m\033")
        print()
        self.slow_print.print_slow("Oh oh! There is a ghost right outside the escape door")
        self.slow_print.print_slow("You need to cast the magic spells to make it go away")
        self.slow_print.print_slow("Here is the 'Harry Potter' series magic spells quiz challenge")
        input("Press ENTER to start the challenge")
        print("\n")
        correct_ans_list, wrong_ans_list = [], []
        self.slow_print.print_slow("Q1. What is the killing curse used by Voldemort to kill Harry in Movie 7 p2 ?")
        self.slow_print.print_slow("A) Crucio B) Avada Kedavra C) Imperio")
        while True:
            first_ans = input("Enter answer: ")
            if first_ans.upper() == "B":
                self.slow_print.print_slow("FANTASTIC! Correct answer")
                correct_ans_list.append("yes")
                break
            elif first_ans.upper() in ["A", "C"]:
                self.slow_print.print_slow("Oops! Wrong answer")
                wrong_ans_list.append("no")
                break
            else:
                print("Invalid input given. Please enter either A, B or C")

        self.slow_print.print_slow("Q2. What magic spell Harry learns in Prisoners of Azkaban (Movie 3) to make"
                                   "Dementors go away ?")
        self.slow_print.print_slow("A) Expecto Patronum B) Sectumsempra  C) Wingardium Leviosa")
        while True:
            first_ans = input("Enter answer: ")
            if first_ans.upper() == "A":
                self.slow_print.print_slow("FANTASTIC! Correct answer")
                correct_ans_list.append("yes")
                break
            elif first_ans.upper() in ["B", "C"]:
                self.slow_print.print_slow("Oops! Wrong answer")
                wrong_ans_list.append("no")
                break
            else:
                print("Invalid input given. Please enter either A, B or C")

        self.slow_print.print_slow("Q3. What is the spell to open the locked doors ?")
        self.slow_print.print_slow("A) Obliviate B) Alohomora  C) Stupefy")
        while True:
            first_ans = input("Enter answer: ")
            if first_ans.upper() == "B":
                self.slow_print.print_slow("FANTASTIC! Correct answer")
                correct_ans_list.append("yes")
                break
            elif first_ans.upper() in ["A", "C"]:
                self.slow_print.print_slow("Oops! Wrong answer")
                wrong_ans_list.append("no")
                break
            else:
                print("Invalid input given. Please enter either A, B or C")

        print('\033[39m')
        if len(correct_ans_list) > len(wrong_ans_list):
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Challenges()
    obj.spooky_lab_escape_challenge()
    obj.escape_door_challenge()
