from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
import sys
import os


def show_logo():
    os.system("cls")
    init(strip=not sys.stdout.isatty())
    print("\n")
    logo = figlet_format("Dropsoft", font="banner3")
    cprint(logo, 'light_cyan')
    print("")


def show_dev_info():
    print("\033[36m" + "VERSION: " + "\033[34m" + "1.0" + "\033[34m")
    print("\033[36m" + "DEV: " + "\033[34m" + "https://t.me/drop_software" + "\033[34m")
    print("\033[36m" +"GitHub: " + "\033[34m" + "https://github.com/Dropsoft-soft/Xterio" + "\033[34m")
    print("\033[36m" + "DONATION EVM ADDRESS: " + "\033[34m" + "0xb1b1ac053248a2C88e32140e4691d2A8Be6Ab9c9" + "\033[0m")
    print()


def show_menu(menu_items: list):
    os.system("")
    print()
    counter = 0
    for item in menu_items:
        counter += 1

        if counter == len(menu_items):
            print('' + '[' + '\033[34m' + f'{counter}' + '\033[0m' + ']' + f' {item}\n')
        else:
            print('' + '[' + '\033[34m' + f'{counter}' + '\033[0m' + ']' + f' {item}')