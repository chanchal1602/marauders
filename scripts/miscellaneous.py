import os
import subprocess
import requests
from urllib.parse import urlparse

def logo():
    print('''
           _   _                       _   _             _        
      ___ | |_| |__   ___ _ __    __ _| |_| |_ __ _  ___| | _____ 
     / _ \| __| '_ \ / _ \ '__|  / _` | __| __/ _` |/ __| |/ / __|
    | (_) | |_| | | |  __/ |    | (_| | |_| || (_| | (__|   <\__ \
     \___/ \__|_| |_|\___|_|     \__,_|\__|\__\__,_|\___|_|\_\___/
    ''')
# menu------------------------------------------------------------
def miscellaneous_menu():
    os.system("clear")
    logo()
    print('''
    [1] Check File Type
    [2] robots.txt
    [3] 
    [9] Back
    [0] Exit
    ''')
    otherattacks_menu()
def file_type():
    file_name= input("Enter file name & extension: ")
    subprocess.call(["file", file_name])
    
def robots():
    website_url = input("Enter the website URL: ")
    find_robots_txt(website_url)

def find_robots_txt(website_url):
    parsed_url = urlparse(website_url)
    hostname = parsed_url.hostname
    robots_txt_url = f"http://{hostname}/robots.txt"
    try:
        response = requests.get(robots_txt_url)
    except requests.exceptions.RequestException as e:
        print("Error fetching robots.txt:", e)
        return None
    if response.status_code == 200:
        # Retrieve the robots.txt content
        robots_txt_content = response.text
        print("Robots.txt content:")
        print(robots_txt_content)
    else:
        print(f"Failed to fetch robots.txt: Status code {response.status_code}")


def otherattacks_menu():
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        logo()
        file_type()
    elif choice == "2":
        os.system('clear')
        logo()
        robots()
    elif choice == "3":
        os.system('clear')
        logo()
    elif choice == "9":
        os.system('clear')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
     miscellaneous_menu()



