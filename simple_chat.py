import socket

def start_server():
    host = socket.gethostname()
    port = int(input("Enter port to listen on: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host,port))

    sock.listen(1)
    print(f"Server started on {host}:{port}. Waiting for a chat partner...")

    conn, addr = sock.accept()
    print(f"Connected to {addr}")

    return conn,sock


def start_client():
    host = input("Enter server IP or hostname: ")
    port = int(input("Enter server port:"))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to {host}:{port}")

    sock.connect((host, port))

    return sock



def chat_menu():
    print("\n--- Simple Chat Module ---")
    print("1. Start Chat Server")
    print("2. Connect to Chat Server")

    choice = input("Select mode (1 or 2 ): ")

    if choice == '1':
        conn, server_sock = start_server()
        #TODO: thread
    elif choice == '2':
        client_sock = start_client()
        #TODO
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    chat_menu()