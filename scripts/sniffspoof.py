import os
def logo():
    print('''
               _  __  __ _                __                      __ _             
     ___ _ __ (_)/ _|/ _(_)_ __   __ _   / /__ _ __   ___   ___  / _(_)_ __   __ _ 
    / __| '_ \| | |_| |_| | '_ \ / _` | / / __| '_ \ / _ \ / _ \| |_| | '_ \ / _` |
    \__ \ | | | |  _|  _| | | | | (_| |/ /\__ \ |_) | (_) | (_) |  _| | | | | (_| |
    |___/_| |_|_|_| |_| |_|_| |_|\__, /_/ |___/ .__/ \___/ \___/|_| |_|_| |_|\__, |
                                 |___/        |_|                            |___/ 

    ''')
# menu------------------------------------------------------------
def main_menu():
    os.system("clear")
    logo()
    print('''
    [1] Sniffing
    [2] Spoofing
    [9] Back
    [0] Exit
    ''')
def menu():
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
    elif choice == "4":
        os.system('clear')
    elif choice == "9":
        os.system('clear')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    menu()



