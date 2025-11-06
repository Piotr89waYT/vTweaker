import os
import subprocess
import time
from colorama import Fore, Style, init

from frontend.mainmenu import *
from backend.globalfunctions.text import *

# Path to the batch file inside a subfolder (example: "tweaks/NetConfig.bat")
bat_path = os.path.join(os.getcwd(), "tweaks", "NetConfig.bat")