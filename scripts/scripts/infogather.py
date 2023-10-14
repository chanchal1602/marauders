#! usr/bin/env python
def scanning():
    print('''
    [1] Host to IP
    [2] IP to Host
    [3] Network Scan(for top 1000 ports)
    [4] TCP Scan
    [5] UDP Scan
    [6] Custom Scan
    [9] Go back
    [0] Exit
    ''')
    
    
    
scanning()
    choice=input("[+]Choose:")
    if choice == "1":
        os.system('clear')
        information_gathering()
    elif choice == "2":
        print("Scanning")
        os.system('clear')
        scanning()
    elif choice == "3":
        print("password attacks")
        os.system('clear')
        password_attack(
