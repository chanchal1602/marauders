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
    [2] Scanning
    [3] Password Attacks
    [4] Exploitation
    [5] Sniffing and Spoofing
    [6] OWASP Top 10
    [7] Other Attack surface
    [8] Report
    [9] Install/ Update
    [0] Exit
    ''')
    choice =0
    choice=input("[+]Choose:")

    if choice == "1":
        os.system('clear')
        infogather_menu()
    elif choice == "2":
        os.system('clear')
    elif choice == "3":
        print("password attacks")
        os.system('clear')
        password_menu()
    elif choice == "4":
        os.system('clear')
        exploitation_menu()
    elif choice == "5":
        print("Sniffing and Spoofing")
        os.system('clear')
        sniffspoof_menu()
    elif choice == "6":
        print("OWASP Top 10")
        os.system('clear')
        owasp_menu()
    elif choice == "7":
        print("Other Attack Surface")
        os.system('clear')
        attack_surface()
    elif choice == "8":
        print("report")
        os.system('clear')
        #implemented for future scope!!!!!
    elif choice == "9":
        print("install/ update")
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
