from slow_print import SlowPrint
import os
import sys
import subprocess


class ModuleDownload(SlowPrint):
    def auto_module_download(self):
        self.print_slow("Installing packages in requirement.txt")
        get_requirement_file = self.check_dir_file_exists("Resources", "requirements.txt")
        if "not found" not in get_requirement_file:
            os.system(f"{sys.executable} -m pip install -r {get_requirement_file}")
        self.print_slow("Packages Installed. Proceeding")

    def run_scenario(self):
        path_of_main = self.check_dir_file_exists("Scripts", "scenario.py")
        subprocess.run([sys.executable, path_of_main])


if __name__ == "__main__":
    obj = ModuleDownload()
    obj.auto_module_download()
    obj.run_scenario()
