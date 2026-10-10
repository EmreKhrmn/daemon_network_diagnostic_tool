import socket

def print_machine_info():
    #hostn name
    host_name = socket.gethostname()

    #primary IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))   #google DNS 
    primary_ip_address = s.getsockname()[0]
    socket_local_port = s.getsockname()[1]
    s.close()

    #all IPs
    all_ips = socket.gethostbyname_ex(host_name)[2]

    print("Host name: %s" % host_name)
    print("Primary IP address: %s" % primary_ip_address)
    print("All IP address(es): %s" % " , ".join(all_ips))
    print("Socket local port: %s" % socket_local_port)


if __name__ == "__main__":
    print_machine_info()