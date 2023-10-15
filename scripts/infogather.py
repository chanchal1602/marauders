import os
import whois
def logo():
    print('''
         _        __                            _   _             
        (_)_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  
        | | '_ \| |_ / _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
        | | | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | |
        |_|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                                                  
                     _   _               _             
          __ _  __ _| |_| |__   ___ _ __(_)_ __   __ _ 
         / _` |/ _` | __| '_ \ / _ \ '__| | '_ \ / _` |
        | (_| | (_| | |_| | | |  __/ |  | | | | | (_| |
         \__, |\__,_|\__|_| |_|\___|_|  |_|_| |_|\__, |
         |___/                                   |___/ ''')
         
'''
inforamtion to be covered is:
domain info
subdomain info
applications tech stack // do reseach how to implement it
public info
email harvesting
social media search
port scanning
    website up or not using ping
    scan types

'''

# menu------------------------------------------------------------
def main_menu():
    os.system("clear")
    logo()
    print('''
    [1] Server Lookup
    [2] IP Address and hosts
    [3] Technology Stack
    [4] Subdomain enumeration
    [5] Port Scanning/ Network Scanning
    [6] dorking
    [7] steganography
    [8] Cryptography
    [9] Back
    [0] Exit
    ''')
def ip_address_and_hosts_menu():
    os.system("clear")
    logo()
    print('''
    [1] IP to Hostname
    [2] Hostname to IP
    [3] Web app status checker
    [0] Exit 
    ''')
def port_scanning_menu():
    os.system("clear")
    logo()
    print('''
    [1] ping scan
    [2] first 1000 port scan
    [3] syn scan
    [4] tcp scan
    [5] udp scan
    [6] verbose scan
    [7] OS scan
    [8] custom scan
    [0] Exit 
    ''')
def dorking_menu():
    os.system("clear")
    logo()
    print('''
    [1] google dorking
    [2] email harvesting
    [3] social media info grabber
    [0] Exit 
    ''')
def cryptography_menu():
    os.system("clear")
    logo()
    print('''
    [1] Encryption
    [2] Decryption
    [3] Encode
    [4] Decode
    [0] Exit 
    ''')
# menu ends-----------------------------------------------------------


def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        print(domain_info)
    except whois.parser.PywhoisError as e:
        print(f"An error occurred: {e}")
def server_lookup():
    domain_name = input("Enter domain name:")
    get_domain_info(domain_name)  
    
    
def infogather_menu():
    main_menu()
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        server_lookup()
    elif choice == "2":
        os.system('clear')
        logo()
        ip_address_and_hosts_menu()
    elif choice == "3":
        os.system('clear')
        logo()
        
    elif choice == "4":
        os.system('clear')
    elif choice == "5":
        os.system('clear')
    elif choice == "6":
        os.system('clear')
    elif choice == "7":
        os.system('clear')
    elif choice == "8":
        os.system('clear')
    elif choice == "9":
        os.system('clear')
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    infogather_menu()



