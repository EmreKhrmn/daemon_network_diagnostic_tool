import socket
import threading

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


def receive_messages(sock, log_filename="chat_log.txt"):

    with open(log_filename, "a", encoding="utf-8") as log_file:
        while True:
            try:
                data = sock.recv(2048)
                if not data:
                    print("[Partner Disconnected]")
                    break

                message = data.decode('utf-8')
                formatted_msg = (f"Partner: {message}")

                print(f"\n{formatted_msg}")
                log_file.write(formatted_msg + "\n")
                log_file.flush()

            except Exception as e:
                print(f"\n[Connection closed or error: {e}]")
                break

def send_messages(sock, log_filename="chat_log.txt"):

    with open(log_filename, "a", encoding="utf-8") as log_file:
        while True:
            try:
                message = input("")
                if message.lower() == 'exit':
                    print("Closing connection...")
                    sock.close()
                    break

                #bytes over network
                sock.sendall(message.encode('utf-8'))

                #own msg log save
                formatted_msg = (f"Me: {message}")
                log_file.write(formatted_msg + "\n")
                log_file.flush()

            except Exception as e:
                break






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