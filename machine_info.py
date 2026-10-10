import socket

def print_machine_info():
    #hostn name
    host_name = socket.gethostname()

    #ip, updated for enviormments without network connectivity
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))   #google DNS 
    primary_ip_address = s.getsockname()[0]
    socket_local_port = s.getsockname()[1]
    s.close()

    print("Host name: %s" % host_name)
    print("Primary IP address: %s" % primary_ip_address)
    print("Socket local port: %s" % socket_local_port)

if __name__ == "__main__":
    print_machine_info()