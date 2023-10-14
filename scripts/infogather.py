import os
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
def main_menu():
    os.system("clear")
    logo()
    print('''
    [1] Server Lookup
    [2] IP Address and hosts
    [3] Technology Stack
    [4] Subdomain enumeration
    [5] Port Scanning/ Network Scanning
    [6] email harvesting
    [7] dorking
    [8] steganography
    [9] Cryptography
    [00] Back
    [0] Exit
    ''')
def ip_address_and_hosts():
    os.system("clear")
    logo()
    print('''
    [1] IP to Hostname
    [2] Hostname to IP
    [3] Web app status checker
    [0] Exit 
    ''')





if __name__ == "__main__":
    infogather()
    import whois

    def get_domain_info(domain_name):
        try:
            domain_info = whois.whois(domain_name)
            print(domain_info)
        except whois.parser.PywhoisError as e:
            print(f"An error occurred: {e}")

    # Example usage
    domain_name = "bitwardha.ac.in"
    get_domain_info(domain_name)

