import socket

def run_server():
    pass

def run_client():
    pass

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





if __name__ == "__main__":
    echo_test_menu()