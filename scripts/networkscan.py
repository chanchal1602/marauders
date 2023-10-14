import socket

def check_port(ip, port):
    """Check if a port is open on a given IP address.

    Args:
        ip (str): The IP address to check.
        port (int): The port to check.

    Returns:
        bool: True if the port is open, False otherwise.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Set a timeout in seconds

    try:
        s.connect((ip, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except socket.error:
        return False
    finally:
        s.close()

def find_open_ports(ip, port_range):
    """Find open ports within a given range on a specific IP address.

    Args:
        ip (str): The IP address to scan.
        port_range (tuple): A tuple representing the range of ports to check.

    Returns:
        list: A list of open ports on the IP address.
    """
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        if check_port(ip, port):
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_ip = "101.53.146.23"
    port_range_to_scan = (1, 30)  # Define the range of ports to scan
    print("scanning for: "+ target_ip+"\n")
    open_ports = find_open_ports(target_ip, port_range_to_scan)
    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip} in the specified range.")

