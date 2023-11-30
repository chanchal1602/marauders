import os
import requests
import sys
#from scripts.adminfinder import admin_main
from scripts.ftpanonlogin import ftp_anon
from time import sleep
def admin_main():
    url = input("Enter your target url: ")  # Get target url from user

    start = "Start Scanning...\n"
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        sleep(0.1)
    file = open("admin_panels.txt", "r")  # Open files containing possible admin directories
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print("*" * 15)
                print("Admin panel found ==> {}".format(curl))
                print("*" * 15)
            else:
                print("\033[91m Not found ==> {} \033[0m".format(curl))
    except KeyboardInterrupt:
        print("\033[91m Shutdown Request! \033[0m")
    except:
        print("\033[91m Unknown Error! \033[0m")
    file.close()


def logo():
    print('''
                                 _         _   _             _    
 _ __   __ _ ___ _____      ____| |   __ _| |_| |_ __ _  ___| | __
| '_ \ / _` / __/ __\ \ /\ / / _` |  / _` | __| __/ _` |/ __| |/ /
| |_) | (_| \__ \__ \\ V  V / (_| | | (_| | |_| || (_| | (__|   < 
| .__/ \__,_|___/___/ \_/\_/ \__,_|  \__,_|\__|\__\__,_|\___|_|\_\
|_|                                                               
                                                                          
    ''')
# menu------------------------------------------------------------
def main_menu():
    os.system("clear")
    logo()
    print('''
    [1] Password Attacks
    [2] Admin page finder
    [9] Back
    [0] Exit
    ''')
def password_menu():
    main_menu()
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        logo()
        attacks_menu()
    elif choice == "2":
        os.system('clear')
        logo()
        admin_main()
    elif choice == "9":
        os.system('clear')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")

def attacks_menu():
    print('''
    [1] Rainbow table
    [2] web app form bruteforce
    [3] ftp anonymous login
    [4] ssh brute
    [9] Back
    [0] Exit
    ''')
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
    elif choice == "2":
        os.system('clear')
        logo()
    elif choice == "3":
        os.system('clear')
        logo()
        ftp_anon()
    elif choice == "4":
        logo()
    elif choice == "9":
        os.system('clear')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")

    
if __name__ == "__main__":
    password_menu()



