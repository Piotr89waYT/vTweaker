import os
from colorama import Fore, Style, init
import shutil

changelogtext = "CHANGELOG"
columns = shutil.get_terminal_size().columns

changelog = '''
----------------------------------------------------------------------------------------------------

Version 1:

- Basic Tweaks added.

----------------------------------------------------------------------------------------------------
'''


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def changelogfunc():
    clear()

    print(f"=" * 120)
    print(" ")
    print(Fore.GREEN + changelogtext.center(columns)) # Prints the Changelog text in green in the middle of the screen
    print(" ")
    print(f"=" * 120)
    print(" ")

    # Prints the changelog text in the middle of the screen
    for line in changelog.strip().splitlines():
        print(Fore.WHITE + line.center(columns))