import os
import subprocess
import time
from colorama import Fore, Style, init

from frontend.mainmenu import *

# Path to the batch file inside a subfolder (example: "tweaks/vTweaks.bat")
bat_path = os.path.join(os.getcwd(), "tweaks", "vTweaks.bat")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tweaks_screen():
    clear()

    print(f"========================================================================================================================")
    print(" ")
    print(f"{Fore.MAGENTA}  [1] > Run Tweaks")
    print(" ")
    print(" ")
    print(" ")
    print(f"{Fore.WHITE} --------------------------------")
    print(f"{Fore.RED} Type 'back' to return to the main screen")
    print(f"{Fore.WHITE} --------------------------------")
    print(" ")
    choice = input(" Enter Option: ").lower()

    if choice == "1":
        clear()

        ps_command = f'Start-Process "cmd.exe" -ArgumentList \'/c "{bat_path}"\' -Verb RunAs -Wait'
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_command])
        
        print(f"{Fore.GREEN} OPERATION COMPLETE")
        time.sleep(1)
        tweaks_screen()

    if choice == "back":
        main()
    

