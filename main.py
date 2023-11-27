# import pyfiglet
#! usr/bin/env python
import time
import scripts
import subprocess
import os
#importing files 
from scripts.infogather import infogather_menu
from scripts.exploitation import exploitation_menu
from scripts.otherattacks import otherattacks_menu
from scripts.owasp10 import owasp_menu
from scripts.passattacks import password_menu
from scripts.sniffspoof import sniffspoof_menu
from scripts.miscellaneous import miscellaneous_menu
#import requests
# comment for me Add other API keys here as needed

#----------
def Mylogo():
    print('''\033[1;32;40m                                                         ██
                                                        ░██
     ██████████   ██████   ██████  ██████   ██   ██     ░██  █████  ██████  ██████
    ░░██░░██░░██ ░░░░░░██ ░░██░░█ ░░░░░░██ ░██  ░██  ██████ ██░░░██░░██░░█ ██░░░░
     ░██ ░██ ░██  ███████  ░██ ░   ███████ ░██  ░██ ██░░░██░███████ ░██ ░ ░░█████
     ░██ ░██ ░██ ██░░░░██  ░██    ██░░░░██ ░██  ░██░██  ░██░██░░░░  ░██    ░░░░░██
     ███ ░██ ░██░░████████░███   ░░████████░░██████░░██████░░██████░███    ██████
    ░░░  ░░  ░░  ░░░░░░░░ ░░░     ░░░░░░░░  ░░░░░░  ░░░░░░  ░░░░░░ ░░░    ░░░░░░''')

    print("\n   \\\---------------Scripted by Arpit, Chanchal, Chirayu, Pranjal---------------//")


# home page menu
def Mainpage():
    print('''
    [1] Information Gathering
    [2] Password Attacks
    [3] Exploitation
    [4] Sniffing and Spoofing
    [5] OWASP Top 10
    [6] miscellaneous
    [7] Install/ Update
    [0] Exit
    ''')
    choice =0
    choice=input("[+]Choose:")

    if choice == "1":
        os.system('clear')
        infogather_menu()
    elif choice == "2":
        print("password attacks")
        os.system('clear')
        password_menu()
    elif choice == "3":
        os.system('clear')
        exploitation_menu()
    elif choice == "4":
        print("Sniffing and Spoofing")
        os.system('clear')
        sniffspoof_menu()
    elif choice == "5":
        print("OWASP Top 10")
        os.system('clear')
        owasp_menu()
    elif choice == "6":
        print(" miscellaneous")
        os.system('clear')
         miscellaneous_menu()
    elif choice == "7":
        os.system('clear')
        print("install/update")
        #print('https://github.com/owasp-amass/amass/blob/master/doc/tutorial.md')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
        
def marauder():
    os.system("clear")
    Mylogo()
    Mainpage()
if __name__ == "__main__":
    marauder()
