import socket


#tcp server
def run_server(port):
    #[OLD]host_name = socket.gethostname()
    host_name = "0.0.0.0"


    #tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #reuse port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #binding
    sock.bind((host_name,port))

    server_log = []
    server_log.append(f"Starting Echo Server on {host_name}:{port}")
    
    #print(f"Starting Echo Server on {host_name}:{port}")
  

    #------------------------
    #send data
    sock.listen(1)

    server_log.append("Waiting for a client to connect...")
    #print("Waiting for a client to connect...")

    conn, addr = sock.accept()
    server_log.append(f"Connected by: {addr}")
    #print(f"Connected by: {addr}")

    with conn:
        while True:
            data = conn.recv(2048)

            if not data:
                break

            server_log.append(f"Received from client. {data.decode('utf-8')}")
            #print(f"Received from client. {data.decode('utf-8')}")

            conn.sendall(data)

    server_log.append("Server connection closed.")
    return "\n".join(server_log)

    






























#tcp client
def run_client(host_name, port, message):
    client_log = []
    
    #[OLD]host_name = input("Enter server IP or hostname to connect to: ")
    
    #[OLD]port = int(input("Enter the server's port: "))

    #tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #[OLD]print(f"Connecting to {host_name}:{port}...")
    client_log.append(f"Connecting to {host_name}:{port}...")

    #connect(?)
    sock.connect((host_name,port))


    try:
        #[OLD]message = input("Please enter your message")
        #[OLD]print(f'Sending "{message}"')
        client_log.append(f'Sending "{message}"')

        sock.sendall(message.encode('utf-8'))

        #response
        amount_received = 0
        amount_expected = len(message)
        full_response = ""

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            full_response += data.decode('utf-8')
            #[OLD]print(f"Received {data}")
            client_log.append(f"Received {data}")

        if message == full_response:
            #[OLD]print(f'Successfully received message: "{full_response}"')
            client_log.append(f'Successfully received message: "{full_response}"')        
        else:    
            #[OLD]print(f'Error: Data mismatch: Received: "{full_response}"')
            client_log.append(f'Error: Data mismatch: Received: "{full_response}"')
    except socket.error as socket_error:
        #[OLD]print(f'Socket error: "{str(socket_error)}"')
        client_log.append(f'Socket error: "{str(socket_error)}"')
    except Exception as exc:
        #[OLD]print(f'Other exception: "{str(exc)}"')
        client_log.append(f'Other exception: "{str(exc)}"')

    finally:
        #[OLD]print("Closing connection to the server")
        client_log.append("Closing connection to the server")
        sock.close()
    return "\n".join(client_log)






















#echo test menu
def echo_test_menu():
    print("\n--- Daemon Echo Test Menu ---")
    print("1. Run as Server")
    print("2. Run as Client")

    choice = input("Select mode (1 or 2): ")

    if choice == '1':
        #terminal fallback, readded inputs here so terminal test still works
        port = int(input("Enter port to listen on: "))
        print(run_server(port))
    elif choice == '2':
        #tterminal fallback, readded inputs here so terminal test still workss
        host_name = input("Enter server IP or hostname to connect to: ")
        port = int(input("Enter the server's port: "))
        message = input("Please enter your message: ")
        print(run_client(host_name, port, message))
    else:
        print("Invalid choice.")

#---------------
if __name__ == "__main__":
    echo_test_menu()