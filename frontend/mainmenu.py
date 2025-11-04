import os
from colorama import Fore, Style, init

from frontend.loadingscreen import *

os.system("mode con: cols=120 lines=40")
user = os.getlogin()
computer = os.getenv('COMPUTERNAME', 'Unknown')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print(Fore.YELLOW + "========================================================================================================================")
    print(f"{Fore.CYAN}  USER: {Fore.WHITE + user}{Fore.CYAN} | COMPUTER NAME: {Fore.WHITE + computer}{Style.RESET_ALL}")
    print(Fore.YELLOW + "========================================================================================================================")
    print(" ")

def options():
    print(f"{Fore.LIGHTMAGENTA_EX} TWEAK")
    print(f"{Fore.WHITE} --------------------------------")
    print(f"{Fore.MAGENTA} [1] | Tweak Options")
    print(f"{Fore.WHITE} --------------------------------")

def changelog():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(f"{Fore.WHITE} --------------------------------")
    print(f"{Fore.RED} [98] | {Fore.WHITE} Check for Updates")
    print(f"{Fore.RED} [99] | {Fore.WHITE} vTweaker Changelog")
    print(f"{Fore.WHITE} --------------------------------")
    print(" ")

def main():
    clear()
    header()
    options()
    changelog()