import os
def logo():
    print('''
           _   _                       _   _             _        
      ___ | |_| |__   ___ _ __    __ _| |_| |_ __ _  ___| | _____ 
     / _ \| __| '_ \ / _ \ '__|  / _` | __| __/ _` |/ __| |/ / __|
    | (_) | |_| | | |  __/ |    | (_| | |_| || (_| | (__|   <\__ \
     \___/ \__|_| |_|\___|_|     \__,_|\__|\__\__,_|\___|_|\_\___/
    ''')
# menu------------------------------------------------------------
def main_menu():
    os.system("clear")
    logo()
    print('''
    [1] Phishing Attacks
    [2] Bruteforce
    [3] Man-In-The Middle Attack
    [9] Back
    [0] Exit
    ''')
def otherattacks_menu():
    main_menu()
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
    elif choice == "2":
        os.system('clear')
        logo()
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
    othrattacks_menu()



