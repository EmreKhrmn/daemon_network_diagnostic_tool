import socket

def run_test(send_buf, recv_buf, timeout_val):
    log = []
    log.append("--- Settings & Error Management Test ---\n")
    
    #socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        return f"Error creating socket: {e}"

    #applying gui settings
    log.append("Applying Settings...")
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, send_buf)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_buf)
        
        #NOTE: DO NOT USE 0.0 FOR TIMEOUT FFS! it auto swaps the socket to non blocking mode
        sock.settimeout(timeout_val) 
    except Exception as e:
        return f"Error applying settings: {e}"

    #r&l the settings
    log.append(f"-> Send Buffer Size: {sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)} bytes")
    log.append(f"-> Recv Buffer Size: {sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)} bytes")
    log.append(f"-> Socket Timeout:   {sock.gettimeout()} seconds")

    #int* error test
    target_host = '192.0.2.1' # dead ip to force a timeout
    target_port = 8080
    
    log.append(f"\nAttempting to connect to {target_host}:{target_port} to test errors...")

    #catching potential errğors
    try:
        sock.connect((target_host, target_port))
    except socket.timeout as e:
        log.append(f"[Caught Error] Connection timed out: {e}")
    except socket.gaierror as e:
        log.append(f"[Caught Error] Address-related error: {e}")
    except socket.error as e:
        log.append(f"[Caught Error] Connection error: {e}")
    finally:
        log.append("\nTest complete. Socket closed securely.")
        sock.close()

    #joins the list into a single text block and sends it to the gui
    return "\n".join(log)

#for use on terminal without gui
if __name__ == '__main__':
    print("\n--- Terminal Settings Test ---")
    s = int(input("Enter Send Buffer (e.g., 4096): "))
    r = int(input("Enter Recv Buffer (e.g., 4096): "))
    t = float(input("Enter Timeout in sec (e.g., 0.5): "))
    
    print("\n" + run_test(s, r, t))