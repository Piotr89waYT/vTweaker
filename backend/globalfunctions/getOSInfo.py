import os
import winreg
import platform
from colorama import Fore, Style, init, Back

init(autoreset=True)

def get_display_version():
    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        ) as key:
            try:
                return winreg.QueryValueEx(key, "DisplayVersion")[0]
            except FileNotFoundError:
                # Older builds use 'ReleaseId'
                return winreg.QueryValueEx(key, "ReleaseId")[0]
    except Exception:
        return "Unknown"

def OSInfo():
    os_name = platform.system()
    edition = "Pro" if "Windows" in os_name else ""
    version = platform.version()
    release = platform.release()
    build = version.split(".")[2] if len(version.split(".")) >= 3 else version
    arch = platform.architecture()[0]
    display_version = get_display_version()

    parts = [
        (Back.BLUE + Fore.WHITE + Style.BRIGHT, f" {os_name} {release} {edition} "),
        (Back.RED + Fore.WHITE + Style.BRIGHT, f" {display_version} "),
        (Back.GREEN + Fore.WHITE + Style.BRIGHT, f" {version} "),
        (Back.CYAN + Fore.WHITE + Style.BRIGHT, f" {build} "),
        (Back.MAGENTA + Fore.WHITE + Style.BRIGHT, f" {arch} "),
    ]

    
    banner_text = Style.BRIGHT + Fore.CYAN + "  CURRENT OS:" + " "
    for style, text in parts:
        banner_text += style + text + Style.RESET_ALL
    return banner_text

