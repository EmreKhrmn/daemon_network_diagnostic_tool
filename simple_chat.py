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


