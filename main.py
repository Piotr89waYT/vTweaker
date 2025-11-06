# Created by Piotr89waYT
#
# For vTweak by .vrx

import os
import time
from colorama import Fore, Style, init

os.system("mode con: cols=120 lines=40")

from backend.globalfunctions.loadingscreen import *
from frontend.mainmenu import *
from frontend.tweaks import *
from frontend.changelog import *

menu_screens = {
    "Home": main,
    "Tweaks": tweaks_screen,
    "Changelog": changelogfunc
}

# Initialize colorama
init(autoreset=True)

def run_app():
    loadingscreenanimation()
    time.sleep(0.3)
    main()

    while True:
        choice = input(" Enter Option: ").strip()

        option_map = {
            "1": "Tweaks",
            "99": "Changelog",
            "back": "Home"
        }

        key = option_map.get(choice)
        if key and key in menu_screens:
            menu_screens[key]()
        else:
            print(f"{Fore.RED} INVALID CHOICE")

if __name__ == "__main__":
    run_app()



