# copyright Jasper Honkasalo 2020

import os
import pyautogui
import time
from colorama import init
from colorama import Fore, Back, Style


init()


def Spam(string, count, delay):
    print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.RED}Starting spam!{Style.RESET_ALL}")
    for x in range(count):
        time.sleep(int(delay) / 1000)
        pyautogui.typewrite(string)
        pyautogui.press("enter")


def SpamFile(filename):
    f = open(filename, 'r')
    print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.RED}Starting spam!{Style.RESET_ALL}")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


def Setup():
    print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} Select mode {Fore.LIGHTBLUE_EX}(file/input): {Style.RESET_ALL}")
    useFile = input()

    if useFile == "file":
        print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} Please input text file name: ")
        fileName = input()
        if os.path.isfile('./' + fileName):
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.GREEN}Found the file.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} Press enter to continue...")
            input()
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.YELLOW}Starting the spam in 5 seconds..!{Style.RESET_ALL}")
            time.sleep(5)
            SpamFile(fileName)
        else:
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.RED}%s.txt file does not exist!{Style.RESET_ALL}" % fileName)
            print()
            Setup()
    elif useFile == "input":
        print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} String to spam: ")
        string = input()
        print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} Spam count: ")
        count = input()
        try:
            val = int(count)
            count = val
        except ValueError:
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.RED}That's not a numerical value!{Style.RESET_ALL}")
            print()
            Setup()
        print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} Delay in ms: ")
        delay = input()
        try:
            value = int(delay)
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} Press enter to continue...")
            input()
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.YELLOW}Starting the spam in 5 seconds..!{Style.RESET_ALL}")
            time.sleep(5)
            Spam(string, count, delay)
        except ValueError:
            print(f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} {Fore.RED}That's not a numerical value!{Style.RESET_ALL}")
            print()
            Setup()
    else:
        print(
            f"{Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} %s {Fore.RED}is not a correct input! Expected either 'y' or 'n'!{Style.RESET_ALL}" % useFile)
        print()
        Setup()


print(f"""{Fore.LIGHTBLUE_EX}{Back.BLACK}
   _____ _____ __  __ _____   _____ 
  / ____|_   _|  \/  |  __ \ / ____|
 | (___   | | | \  / | |__) | (___  
  \___ \  | | | |\/| |  ___/ \___ \ 
  ____) |_| |_| |  | | |     ____) |
 |_____/|_____|_|  |_|_|    |_____/      
{Style.RESET_ALL}""")
for x in range(7):
    time.sleep(0.3)
    print()
print(f"Welcome to {Fore.CYAN}{Back.BLACK}[SIMPS]{Style.RESET_ALL} (SIMple - Python - Spammer) by Jasper Honkasalo!")
time.sleep(0.3)
print()
time.sleep(0.3)
print()
time.sleep(0.3)
print(f"{Fore.CYAN}{Back.BLACK}[SIMPS - Warning] {Style.RESET_ALL}{Fore.YELLOW}Quit the script with 'ctrl+c' at any time!{Style.RESET_ALL}")
time.sleep(0.3)
Setup()
