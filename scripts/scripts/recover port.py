# functions starts here------------------------------

  ##infomration gathering

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



