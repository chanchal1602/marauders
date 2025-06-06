# import pyfiglet
#! usr/bin/env python
import time
import scripts
import subprocess
import os
#importing files 
from scripts.infogather import infogather_menu
from scripts.exploitation import exploitation_menu
from scripts.owasp10 import owasp_menu
from scripts.passattacks import password_menu
from scripts.webattack import web_attack_menu
from scripts.miscellaneous import miscellaneous_menu
from scripts.adminfinder import admin_main
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

    print("\n   \\\---------------Scripted by Chanchal---------------//")


# home page menu
def Mainpage():
    print('''
    [1] Information Gathering
    [2] Password Attacks
    [3] Web attacks
    [4] OWASP Top 10
    [5] miscellaneous
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
        print("Web Attack Tools")
        os.system('clear')
        web_attack_menu()
    elif choice == "4":
        print("OWASP Top 10")
        os.system('clear')
        owasp_menu()
    elif choice == "5":
        print(" miscellaneous")
        os.system('clear')
        miscellaneous_menu()
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
