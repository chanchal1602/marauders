# import pyfiglet

import os
import requests
# Add your API keys here
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
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
    print("[+]choose:")

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


if __name__ == "__main__":
    Mylogo()
    Mainpage()

def shodan_search():
    print("You selected Shodan")
    ip_address = input("Enter the IP address you want to search: ")
    response = requests.get(f"https://api.shodan.io/shodan/host/{ip_address}", headers={"Authorization": f"Bearer {SHODAN_API_KEY}"})
    if response.status_code == 200:
        print("Shodan Response:")
        print(response.text)
    else:
        print("Error connecting to Shodan API.")

def onyphe_search():
    print("You selected Onyphe")
    target = input("Enter the IP address or domain you want to search: ")
    response = requests.get(f"https://api.onyphe.io/v1/ip/{target}?apikey={ONYPHE_API_KEY}")
    if response.status_code == 200:
        print("Onyphe Response:")
        print(response.text)
    else:
        print("Error connecting to Onyphe API.")

def ivre_search():
    print("You selected Ivre")
    target = input("Enter the IP address or domain you want to search: ")
    response = requests.get(f"https://api.ivre.com/endpoint?apikey=YOUR_IVRE_API_KEY&target={target}")
    if response.status_code == 200:
        print("Ivre Response:")
        print(response.text)
    else:
        print("Error connecting to Ivre API.")

def main():
    print("Marauders")
    while True:
        print("Select an option:")
        print("1. Server")
        print("2. Dorks")
        print("3. WiFi Networks")
        print("4. Code Search")
        print("5. Thread Intelligence")
        print("6. OSINT")
        print("7. Email Addresses")
        print("8. Attack Surface")
        print("9. Certificate Search")
        print("10. Vulnerabilities")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You selected Server")
            print("Select a sub-option:")
            print("1. Shodan")
            print("2. Onyphe")
            print("3. Ivre")
            sub_choice = input("Enter your sub-choice: ")

            if sub_choice == "1":
                shodan_search()
            elif sub_choice == "2":
                onyphe_search()
            elif sub_choice == "3":
                ivre_search()
            else:
                print("Invalid sub-choice. Please select a valid option.")
        # Add code for other menu options here
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")



