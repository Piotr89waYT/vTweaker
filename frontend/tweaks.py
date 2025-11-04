import os
from colorama import Fore, Style, init

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tweaks_screen():
    clear()
    print(f"{Fore.RED} WORK IN PROGRESS")
    pass
