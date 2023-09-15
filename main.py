# import pyfiglet
#! usr/bin/env python
import time
import subprocess
import os
import requests
# Add your API keys here
# google maps api keyscc
SHODAN_API_KEY = "bm2DmZaQIEw5oXcOVx4qy3HPXF5PrjZi"
ONYPHE_API_KEY = "YOUR_ONYPHE_API_KEY"
WIGLE_API_KEY = "YOUR_WIGLE_API_KEY"
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GREP_APP_API_KEY = "YOUR_GREP_APP_API_KEY"
SEARCHCODE_API_KEY = "YOUR_SEARCHCODE_API_KEY"
PUBLICWWW_API_KEY = "YOUR_PUBLICWWW_API_KEY"
INTELX_API_KEY = "YOUR_INTELX_API_KEY"
HUNTER_API_KEY = "YOUR_HUNTER_API_KEY"
BINARYEDGE_API_KEY = "YOUR_BINARYEDGE_API_KEY"
FULLHUNT_API_KEY = "YOUR_FULLHUNT_API_KEY"
NELAS_API_KEY = "YOUR_NELAS_API_KEY"
# Add other API keys here as needed

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
    [5] Post-Exploitation
    [6] Sniffing and Spoofing
    [7] Web Hacking
    [8] Report
    [9] Install/ Update
    [0] Exit
    ''')
    choice=input("[+]Choose:")

    if choice == "1":
        os.system('clear')
        information_gathering()
    elif choice == "2":
        print("Scanning Phase under construction")
    elif choice == "2":
        print("password attacks")
    elif choice == "2":
        print("Exploitation")
    elif choice == "2":
        print("post Exploitation")
    elif choice == "2":
        print("sniffing and spoofing")
    elif choice == "2":
        print("web hacking")
    elif choice == "2":
        print("report")
    elif choice == "2":
        print("install/ update")
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")

def information_gathering():
    print('''
    [1] Server lookups
    [2] MAC Address Changer
    [3] Google Dorks
    [4] Email Harvesting
    [5] Certificates search
    [0] Exit
    ''')
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        Server_lookup()
    elif choice == "2":

        print("")
    elif choice == "2":
        print("")
    elif choice == "2":
        print("")
    elif choice == "2":
        print("")
    elif choice == "0":
        return

def Server_lookup():
    site=input("[+]Enter the name of target:")
    os.system('whois '+site)
def 
if __name__ == "__main__":
    Mylogo()
    Mainpage()
