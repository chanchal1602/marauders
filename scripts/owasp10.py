import os
from scripts.rxss import xssmain
from scripts.lfi import entryy
from scripts.owaspquick import quick_scan
def logo():
    print('''
                                _                _  ___  
  _____      ____ _ ___ _ __   | |_ ___  _ __   / |/ _ \ 
 / _ \ \ /\ / / _` / __| '_ \  | __/ _ \| '_ \  | | | | |
| (_) \ V  V / (_| \__ \ |_) | | || (_) | |_) | | | |_| |
 \___/ \_/\_/ \__,_|___/ .__/   \__\___/| .__/  |_|\___/ 
                       |_|              |_|              

    ''')
# menu------------------------------------------------------------
def main_menu():
    os.system("clear")
    logo()
    print('''
    [1] XSS attack
    [2] SQL Injection
    [3] Local File Inclusion
    [4] owasp quick scan
    [99] Back
    [0] Exit
    ''')
def owasp_menu():
    main_menu()
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        logo()
        xssmain()
    elif choice == "2":
        os.system('clear')
        logo()
    elif choice == "3":
        os.system('clear')
        logo()
        entryy()
    elif choice == "4":
        os.system('clear')
        logo()
        quick_scan()
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
        
if __name__ == "__main__":
    owasp_menu()



