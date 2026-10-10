import socket

def print_machine_info():
    #hostn name
    host_name = socket.gethostname()

    #ip, updated for enviormments without network connectivity
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))   #google DNS 
    ip_address = s.getsockname()[0]
    s.close()

    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)

if __name__ == "__main__":
    print_machine_info()