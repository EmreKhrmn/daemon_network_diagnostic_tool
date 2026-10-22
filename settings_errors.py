import socket
import sys

def test_settings_and_errors():
    print("--- Settings & Error Management Test")

    #false ip
    target_host = '192.0.2.1'
    target_port = 8080

    #socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error creating socket: {e}")
        sys.exit(1)

 