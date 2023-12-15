import socket
import ipaddress
import concurrent.futures

def get_local_ip():
    # Get the local machine's IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

def is_host_alive(ip):
    # Check if the host is reachable
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, 80))
    sock.close()
    return result == 0

def scan_ip(ip):
    try:
        if is_host_alive(ip):
            hostname = socket.gethostbyaddr(ip)[0]
            return {'ip': ip, 'hostname': hostname}
    except (socket.herror, socket.error):
        pass
    return None

def scan_local_network():
    local_ip = get_local_ip()
    network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)

    devices = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_ip, str(ip)) for ip in network.hosts()]
        devices = [future.result() for future in concurrent.futures.as_completed(futures) if future.result()]

    return devices

def main():
    print("Scanning devices on the local network...\n")

    devices = scan_local_network()

    if not devices:
        print("No active devices found.")
        return

    print("Discovered devices:")
    for device in devices:
        print(f"Hostname: {device['hostname']}, IP Address: {device['ip']}")

if __name__ == "__main__":
    main()
