import os
def logo():
    print('''
                     _       _ _        _   _             
      _____  ___ __ | | ___ (_) |_ __ _| |_(_) ___  _ __  
     / _ \ \/ / '_ \| |/ _ \| | __/ _` | __| |/ _ \| '_ \ 
    |  __/>  <| |_) | | (_) | | || (_| | |_| | (_) | | | |
     \___/_/\_\ .__/|_|\___/|_|\__\__,_|\__|_|\___/|_| |_|
              |_|                                         
    ''')
# menu------------------------------------------------------------
def main_menu():
    os.system("clear")
    logo()
    print('''
    [1] Wordlists
    [2] Password Attacks
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
        wordlist_menu()
    elif choice == "9":
        os.system('clear')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
def wordlist_menu():   
    print('''
    [1] Crunch
    [2] Seclist(already created)
    [3] rockyou(already created)
    [4] CUPP
    [9] Back
    [0] Exit
    ''')
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
    elif choice == "2":
        os.system('clear')
        logo()
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
    [3] hydra
    [9] Back
    [0] Exit
    ''')
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
    elif choice == "2":
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
    password_menu()



