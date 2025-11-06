import os
import platform
from colorama import Fore, Style, init, Back

from backend.globalfunctions.loadingscreen import *
from backend.globalfunctions.getOSInfo import *

os.system("mode con: cols=120 lines=40")
user = os.getlogin()
computer = os.getenv('COMPUTERNAME', 'Unknown')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header():
    print(f"{Fore.YELLOW}=" * 120)
    print(f"{Fore.CYAN}  USER: {Fore.WHITE + user}{Fore.CYAN} | COMPUTER NAME: {Fore.WHITE + computer}{Style.RESET_ALL}")
    print(OSInfo())
    print(f"{Fore.YELLOW}=" * 120)
    print()

def options():
    print(f"{Fore.LIGHTMAGENTA_EX} TWEAKS")
    print(f"{Fore.WHITE} -" + "-" * 32)
    print(f"{Fore.MAGENTA} [1] | Tweak Options")
    print(f"{Fore.MAGENTA} [2] | Network Options")
    print(f"{Fore.WHITE} -" + "-" * 32)

def changelog():
    print()
    print()
    print()
    print()
    print()
    print()
    print(f"{Fore.WHITE} -" + "-" * 32)
    print(f"{Fore.RED} [98] | {Fore.WHITE} Check for Updates")
    print(f"{Fore.RED} [99] | {Fore.WHITE} vTweaker Changelog")
    print(f"{Fore.WHITE} -" + "-" * 32)
    print()

def main():
    clear()
    header()
    options()
    changelog()