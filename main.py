import machine_info
import echo_test

def main():
    #temporary menu skeleton
    while True:
        print("\n ---Daemon Menu---")
        print("1. Machine Information")
        print("2. Echo Test")
        print("3. SNTP Time Synchronization")
        print("4. Simple Chat")
        print("5. Error Management and Settings")
        print("0. Exit")
    
        choice = input("Choose an option (0-5): ")

        if choice == '1':
            machine_info.print_machine_info()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '0':
            print("Exiting the menu.")   
            break
        else:
            print("Invalid choice. Please select a valid option.")


    
    pass




if __name__ == "__main__":
    main()