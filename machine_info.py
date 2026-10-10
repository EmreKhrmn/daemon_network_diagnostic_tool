import socket
import psutil


def print_machine_info():
    #hostn name
    host_name = socket.gethostname()

    #primary IP & Socket local port
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))   #google DNS 
    primary_ip_address = s.getsockname()[0]
    socket_local_port = s.getsockname()[1]
    s.close()

    #all IPs
    all_ips = socket.gethostbyname_ex(host_name)[2]

    #network interfaces and their IPs/MAC's and their names
    def get_network_interfaces():

        network_interfaces = psutil.net_if_addrs()
        #list_of_network_interface = loni
        loni = []

        for interface_name, addresses in network_interfaces.items():
            #name
            loni.append(f"\nInterface Name: {interface_name}")

            #addresses
            for addr in addresses:
                #IPv4 addresses
                if addr.family == socket.AF_INET:
                    loni.append(f" IPv4 Address: {addr.address}")
                    loni.append(f" Netmask:      {addr.netmask}")
                #Mac addresses
                elif addr.family == psutil.AF_LINK:
                    loni.append(f" MAC Address:  {addr.address}")

        return "\n".join(loni)
        



    #printing machine info
    print(f"Host name: {host_name}\n")
    print(f"Primary IP address: {primary_ip_address}\n")
    print(f"All IP address(es): {" , ".join(all_ips)}\n")
    print(f"Socket local port: {socket_local_port}\n")
    print(f"List Of Network Interfaces: \n{get_network_interfaces()}\n")


if __name__ == "__main__":
    print_machine_info()