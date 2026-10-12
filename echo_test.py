import socket


#tcp server
def run_server():
    host_name = socket.gethostname()

    port = int(input("Enter port to listen on: "))

    #tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #reuse port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #binding
    sock.bind((host_name,port))

    print(f"Starting Echo Server on {host_name}:{port}")
  

    #------------------------
    #send data
    sock.listen(backlog)
    






























#tcp client
def run_client():
    host_name = input("Enter server IP or hostname to connect to: ")
    
    port = int(input("Enter the server's port: "))

    #tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"Connecting to {host_name}:{port}...")

    #connect(?)
    sock.connect((host_name,port))


    try:
        message = input("Please enter your message")
        print(f'Sending "{message}"')

        sock.sendall(message.encode('utf-8'))

        #response
        amount_received = 0
        amount_expected = len(message)
        full_response = ""

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            full_response += data.decode('utf-8')
            print(f"Received {data}")

        if message == full_response:
            print(f'Successfully received message: "{full_response}"')
        else:    
            print(f'Error: Data mismatch: Received: "{full_response}"')
    except socket.error as socket_error:
        print(f'Socket error: "{str(socket_error)}"')

    except Exception as exc:
        print(f'Other exception: "{str(exc)}"')

    finally:
        print("Closing connection to the server")

        sock.close()























#echo test menu
def echo_test_menu():
    print("\n--- Daemon Echo Test Menu ---")
    print("1. Run as Server")
    print("2. Run as Client")

    choice = input("Select mode (1 or 2): ")

    if choice == '1':
        run_server()
    elif choice == '2':
        run_client()
    else:
        print("Invalid choice.")

#---------------
if __name__ == "__main__":
    echo_test_menu()