import os

import requests
from scripts.adminfinder import admin_main

def logo():
    print('''
web attack
    ''')
# menu------------------------------------------------------------
def web_attack_menu():
    os.system("clear")
    logo()
    print('''
    [1] admin finder
    [2] Directory Bruteforce
    [9] Back
    [0] Exit
    ''')
    choice=input("[+]Choose:")
    if choice == "1":
        #os.system('clear')
        admin_main()
    elif choice == "2":
        os.system('clear')
        logo()
        dir_brute()
    elif choice == "3":
        os.system('clear')
        logo()
    elif choice == "4":
        os.system('clear')
    elif choice == "9":
        os.system('clear')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
        
def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
def dir_brute():
    targetURL = input("Enter Target URL: ")
    file = open("common.txt", "r")
    for line in file:
        line = line.strip('\n')
        fullURL = targetURL + "/" + line
        response = request(fullURL)
        if response:
            print('[+] Discovered Directory at Link: ' + fullURL)
        
        
if __name__ == "__main__":
    web_attack_menu()



