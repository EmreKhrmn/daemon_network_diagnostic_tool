import socket
import threading

def start_server_socket(port):

    host = "0.0.0.0"
    #host = socket.gethostname()
    #[REMOVED]port = int(input("Enter port to listen on: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host,port))

    sock.listen(1)
    print(f"Server started on {host}:{port}. Waiting for a chat partner...")

    conn, addr = sock.accept()
    print(f"Connected to {addr}")

    return conn


def start_client_socket(host, port):
    #[REMOVED]host = input("Enter server IP or hostname: ")
    #[REMOVED]port = int(input("Enter server port:"))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to {host}:{port}")

    sock.connect((host, port))

    return sock


def receive_messages_gui(sock, ui_callback, log_filename="chat_log.txt"):

    #[removed][fix]with open(log_filename, "a", encoding="utf-8") as log_file:
        while True:
            try:
                data = sock.recv(2048)
                if not data:
                    #[REMOVED]print("[Partner Disconnected]")
                    ui_callback("[Partner Disconnected]")
                    break

                message = data.decode('utf-8')
                formatted_msg = (f"Partner: {message}")

                ui_callback(formatted_msg)
                #[REMOVED]print(f"\n{formatted_msg}")
                #[removed][fix]log_file.write(formatted_msg + "\n")
                #[removed][fix]log_file.flush()
                with open(log_filename, "a", encoding="utf-8") as log_file:
                    log_file.write(formatted_msg + "\n")

            except Exception as e:
                #[REMOVED]print(f"\n[Connection closed or error: {e}]")
                ui_callback(f"[Connection closed or error: {e}]")
                break




def send_message_net(sock, message, log_filename="chat_log.txt"):

    with open(log_filename, "a", encoding="utf-8") as log_file:
        try:
            if message.lower() == 'exit':
                print("Closing connection...")
                sock.close()
                return

                #bytes over network
                sock.sendall(message.encode('utf-8'))

                #own msg log save
                formatted_msg = (f"Me: {message}")
                log_file.write(formatted_msg + "\n")
                log_file.flush()

        except Exception as e:
            pass






def chat_menu():
    print("\n--- Simple Chat Module ---")
    print("1. Start Chat Server")
    print("2. Connect to Chat Server")

    choice = input("Select mode (1 or 2 ): ")

    if choice == '1':
        #conn, server_sock = start_server()
        port = int(input("Enter port to listen on: "))
        conn = start_server_socket(port)
        print("Chat Started. Type your message below. Type 'exit' to quit.")

        #receiver
        recv_thread = threading.Thread(target=receive_messages_gui, args=(conn, print))
        recv_thread.daemon = True
        recv_thread.start()

        #sender
        #[REMOVED]send_messages(conn)

        #clean
        #[REMOVED]conn.close()
        #[REMOVED]server_sock.close()

        while True:
            msg = input("")
            if msg.lower() == 'exit':
                conn.close()
                break
            send_message_net(conn, msg)


    elif choice == '2':
        #[REMOVED]client_sock = start_client()
        host = input("Enter server IP or hostname: ")
        port = int(input("Enter server port: "))
        client_sock = start_client_socket(host, port)

        print("Chat started. Type your message below. Type 'exit' to quit." )

        recv_thread = threading.Thread(target=receive_messages_gui, args=(client_sock, print))
        recv_thread.daemon = True
        recv_thread.start()

        #[REMOVED]send_messages(client_sock)
        while True:
            msg = input("")
            if msg.lower() == 'exit':
                client_sock.close()
                break
            send_message_net(client_sock, msg)
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    chat_menu()