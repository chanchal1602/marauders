import os
import subprocess
import socket
import sys
import base64
import time
import whois
# from __future__ import print_function
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
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        logo()
        ip_to_host()
    elif choice == "2":
        os.system('clear')
        logo()
        host_to_ip()
    elif choice == "3":
        os.system('clear')
def port_scanning_menu():
    os.system("clear")
    logo()
    print('''
    [1] ping scan
    [2] first 1000 port scan
    [3] script scan scan
    [4] service version scan
    [5] udp scan
    [6] verbose scan
    [7] OS scan
    [8] custom scan
    [0] Exit 
    ''')
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        logo()
        nmap_sn() #ping scan
    elif choice == "2":
        os.system('clear')
        logo()
        nmap_1000() # top 1000 ports scan 
    elif choice == "3":
        os.system('clear')
        logo()
        nmap_sC()   # script scan
    elif choice == "4":
        os.system('clear')
        logo()
        nmap_sV()  #service version
    elif choice == "5":
        os.system('clear')
    elif choice == "6":
        os.system('clear')
    elif choice == "7":
        os.system('clear')
        logo()
        nmap_o()   #operating system scan
    elif choice == "8":
        os.system('clear')
    elif choice == "0":
        return
    else:
        print('Invalid input try again!!!!!!!!!')
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
    choice=input("[+]Choose:")
    if choice == "3":
        os.system('clear')
        logo()
        print('''
    [1] base64
    [9] back
    [0] Exit 
    ''')
        choice=input("[+]Choose:")
        if choice == "1":
            e_base64()
        elif choice == "0":
            return
    elif choice == "4":
        print('''
    [1] base64
    [9] back
    [0] Exit 
    ''')
        choice=input("[+]Choose:")
        if choice == "1":
            d_base64()
        elif choice == "0":
            return
    elif choice == "0":
        return
    else:
        print("You entered invalid choice!!!!!!!!!!!")
# menu ends-----------------------------------------------------------

# functions for scripts starts here-----------------------------------
    # cryptography script starts here---------------------------------
def encode_base64(text):
    encoded_text = base64.b64encode(text.encode("utf-8"))
    return encoded_text.decode("utf-8")
def decode_base64(encoded_text):
    decoded_text = base64.b64decode(encoded_text.encode("utf-8"))
    return decoded_text.decode("utf-8")
def e_base64():
    text =input("Enter the text: ")
    encoded_text = encode_base64(text)
    print("Encoded text:", encoded_text)

def d_base64():
    text =input("Enter the text: ")
    decoded_text = decode_base64(text)
    print("Decoded text:", decoded_text)
    
    # function for website information-----------------------------------
def execute_whatweb(url):
    try:
        # Use the subprocess module to execute the whatweb command
        subprocess.call(["whatweb", url])
    except Exception as e:
        print("Error executing whatweb command:", e)
def tech_stack_info():
    url = input("Enter the URL: ")
    execute_whatweb(url)
    
    # functions for domain information-----------------------------------
def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        print(domain_info)
    except whois.parser.PywhoisError as e:
        print(f"An error occurred: {e}")
def server_lookup():
    domain_name = input("Enter domain name:")
    get_domain_info(domain_name)  
    
    # functions to convert an IP address to hostname-----------------------------------
def convert_ip_to_hostname(ip_address):
  try:
    hostname, aliases, addresses = socket.gethostbyaddr(ip_address)
    return hostname
  except socket.gaierror:
    return None
    

def ip_to_host():
  ip_address = input("Enter an IP address: ")
  hostname = convert_ip_to_hostname(ip_address)

  if hostname is None:
    print("The IP address could not be found.")
  else:
    print("The hostname is {}.".format(hostname))

    # functions to convert website name into ip address ----------------------------------
def convert_website_name_to_ip_address(website_name):
  try:
    ip_address = socket.gethostbyname(website_name)
    return ip_address
  except socket.gaierror:
    return None

def host_to_ip():
    website_name = input("Enter a website name: ")
    ip_address = convert_website_name_to_ip_address(website_name)

    if ip_address is None:
        print("The website name could not be resolved.")
    else:
        print("The IP address of the website name is {} ".format(ip_address))
        
        
# nmap scan starts here---------------------------------------------------------------------
    # nmap script scan i.e. nmap -sC <ip/ hostname>
def nmap_output_sC(nmap_output):
   for line in nmap_output.splitlines():
    print(line)
    
def nmap_sC():
    # Run the nmap command.
    websitename=input('Enter the website name for scan:   ')
    nmap_output = subprocess.check_output(["nmap", "-sC", websitename])

    # Decode the nmap output.
    nmap_output = nmap_output.decode()

    # Print the nmap output to the console.
    nmap_output_sC(nmap_output)

    # nmap service version scan i.e. nmap -sV <ip/ hostname>
def namp_output_sV(command):
 
  output = subprocess.check_output(command)
  return output.decode()

def nmap_sV():

  # Execute the nmap command and get the output.
  website=input('Enter website name: ')
  output = namp_output_sV(["nmap", "-sV", website])

  # Print the output to the console.
  print(output)
  
  #nmap top 1000 ports quick scan

def nmap_output_1000(target_ip_address, port_range="1-1000"):
 
  command = ["nmap", "-p", port_range, target_ip_address]
  output = subprocess.check_output(command)
  return output.decode()

def nmap_1000():
  # Get the target IP address from the user.
  target_ip_address = input("Enter the IP address of the target host: ")
  output = nmap_output_1000(target_ip_address)

  # Print the output to the console.
  print(output)

def nmap_output_o(target_ip_address, options=""):

  command = ["nmap", options, target_ip_address]
  output = subprocess.check_output(command)
  return output.decode()

def nmap_o():

  # Get the target IP address from the user.
  target_ip_address = input("Enter the IP address of the target host: ")

  # Execute the Nmap scan and get the output.
  output = nmap_output_o(target_ip_address, options="-O")

  # Print the output to the console.
  print(output)




#elif ladder for showing the root menu page------------------------------------

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
        tech_stack_info()
    elif choice == "4":
        os.system('clear')
        logo()
    elif choice == "5":
        os.system('clear')
        logo()
        port_scanning_menu()
    elif choice == "6":
        os.system('clear')
        logo()
        dorking_menu()
    elif choice == "7":
        os.system('clear')
    elif choice == "8":
        os.system('clear')
        logo()
        cryptography_menu()
    elif choice == "9":
        os.system('clear')
        infogather_menu()
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please select a valid option.")
        
        
# main function starts here---------------------------------------------
if __name__ == "__main__":
    infogather_menu()


    
