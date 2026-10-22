#lib
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import sys

#modules
import machine_info
import echo_test
import sntp_time
import simple_chat

class DaemonGUI:
#------------------------------------------------------------------------------------------------------------------------
    def __init__(self, root):
        self.root = root
        self.root.title("Daemon Network Diagnostic Tool")
        self.root.geometry("800x600")

        #tab control
        self.tabs = ttk.Notebook(root)

        #frame for each tab
        self.tab_info = ttk.Frame(self.tabs)
        self.tab_echo = ttk.Frame(self.tabs)
        self.tab_sntp = ttk.Frame(self.tabs)
        self.tab_chat = ttk.Frame(self.tabs)
        self.tab_settings = ttk.Frame(self.tabs)

        #tabs
        self.tabs.add(self.tab_info, text='A. Machine Info')
        self.tabs.add(self.tab_echo, text='B. Echo Test')
        self.tabs.add(self.tab_sntp, text='C. SNTP Time')
        self.tabs.add(self.tab_chat, text='D. Simple Chat')
        self.tabs.add(self.tab_settings, text='E. Settings & Errors')

        self.tabs.pack(expand=1, fill="both")

        self.build_info_tab()
        self.build_echo_tab()
        self.build_sntp_tab()
        self.build_chat_tab()
        self.build_settings_tab()
#------------------------------------------------------------------------------------------------------------------------
    #module A / machine info
    def build_info_tab(self):
        ttk.Label(self.tab_info, text="Machine Information", font=("Arial", 14, "bold")).pack(pady=10)
            
        self.info_output = scrolledtext.ScrolledText(self.tab_info, width=80, height=20)
        self.info_output.pack(pady=10, padx=20)
            
        ttk.Button(self.tab_info, text="Get Machine Info", command=self.run_machine_info).pack(pady=10)


    def run_machine_info(self):
        self.info_output.delete(1.0, tk.END)
        try:
            #call machine info file
            result = machine_info.get_info() 
            self.info_output.insert(tk.END, result)
        except Exception as e:
            self.info_output.insert(tk.END, f"Error loading module: {e}")

#------------------------------------------------------------------------------------------------------------------------
    #module B /echo test
    def build_echo_tab(self):
        ttk.Label(self.tab_echo, text="Echo Client/Server Test", font=("Arial", 14, "bold")).pack(pady=10)

        #settings frame
        frame = ttk.Frame(self.tab_echo)
        frame.pack(pady=5)
        
        ttk.Label(frame, text="Target IP:").grid(row=0, column=0, padx=5)
        self.echo_ip = ttk.Entry(frame, width=15)
        self.echo_ip.insert(0, "127.0.0.1")
        self.echo_ip.grid(row=0, column=1, padx=5)
        
        ttk.Label(frame, text="Port:").grid(row=0, column=2, padx=5)
        self.echo_port = ttk.Entry(frame, width=10)
        self.echo_port.insert(0, "9900")
        self.echo_port.grid(row=0, column=3, padx=5)

        #button
        btn_frame = ttk.Frame(self.tab_echo)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Start Echo Server", command=self.start_echo_server).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Send Echo Client", command=self.send_echo_client).grid(row=0, column=1, padx=10)

        self.echo_output = scrolledtext.ScrolledText(self.tab_echo, width=80, height=15)
        self.echo_output.pack(pady=10)

    def start_echo_server(self):
        port = int(self.echo_port.get())
        self.echo_output.insert(tk.END, f"Starting Echo Server on port {port}...\n")
        #running server in background
        threading.Thread(target=self._run_echo_server_thread, args=(port,), daemon=True).start()

    def _run_echo_server_thread(self, port):
        try:
            #callin ecdho file
            result = echo_test.run_server(port)
            self.echo_output.insert(tk.END, f"{result}\n")
        except Exception as e:
            self.echo_output.insert(tk.END, f"Server Error: {e}\n")

    def send_echo_client(self):
        ip = self.echo_ip.get()
        port = int(self.echo_port.get())
        msg = "Echo Test Message"
        self.echo_output.insert(tk.END, f"Connecting to {ip}:{port}...\n")
        
        threading.Thread(target=self._run_echo_client_thread, args=(ip, port, msg), daemon=True).start()

    def _run_echo_client_thread(self, ip, port, msg):
        try:
            #calling echo file
            result = echo_test.run_client(ip, port, msg)
            self.echo_output.insert(tk.END, f"{result}\n")
        except Exception as e:
            self.echo_output.insert(tk.END, f"Client Error: {e}\n")    

#------------------------------------------------------------------------------------------------------------------------
# module C / sntp time
    def build_sntp_tab(self):
        ttk.Label(self.tab_sntp, text="SNTP Time Synchronization", font=("Arial", 14, "bold")).pack(pady=10)
        self.sntp_output = scrolledtext.ScrolledText(self.tab_sntp, width=80, height=10)
        self.sntp_output.pack(pady=10)
        ttk.Button(self.tab_sntp, text="Fetch Time", command=self.run_sntp).pack(pady=10)

    def run_sntp(self):
        self.sntp_output.delete(1.0, tk.END)
        self.sntp_output.insert(tk.END, "Requesting time...\n")
        self.root.update()
        try:
            #calls sntp file
            result = sntp_time.get_sntp_time()
            self.sntp_output.insert(tk.END, f"\n{result}")
        except Exception as e:
            self.sntp_output.insert(tk.END, f"\nError fetching time: {e}")

#------------------------------------------------------------------------------------------------------------------------

#module D /simple chat

    def build_chat_tab(self):
        ttk.Label(self.tab_chat, text="Simple Chat", font=("Arial", 14, "bold")).pack(pady=10)
        
        #connection controls
        conn_frame = ttk.Frame(self.tab_chat)
        conn_frame.pack(pady=5)
        
        ttk.Label(conn_frame, text="IP:").grid(row=0, column=0, padx=5)
        self.chat_ip = ttk.Entry(conn_frame, width=15)
        self.chat_ip.insert(0, "127.0.0.1")
        self.chat_ip.grid(row=0, column=1, padx=5)
        
        ttk.Label(conn_frame, text="Port:").grid(row=0, column=2, padx=5)
        self.chat_port = ttk.Entry(conn_frame, width=10)
        self.chat_port.insert(0, "8888")
        self.chat_port.grid(row=0, column=3, padx=5)

        ttk.Button(conn_frame, text="Host Chat (Server)", command=self.host_chat).grid(row=0, column=4, padx=5)
        ttk.Button(conn_frame, text="Join Chat (Client)", command=self.join_chat).grid(row=0, column=5, padx=5)

        #chat log box
        self.chat_log = scrolledtext.ScrolledText(self.tab_chat, width=80, height=15, state='disabled')
        self.chat_log.pack(pady=10)

        #message entry and send
        msg_frame = ttk.Frame(self.tab_chat)
        msg_frame.pack(fill='x', padx=20)
        self.chat_entry = ttk.Entry(msg_frame)
        self.chat_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        ttk.Button(msg_frame, text="Send", command=self.send_chat_msg).pack(side='right')

        self.chat_socket = None #hold

    def log_chat(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.yview(tk.END)
        self.chat_log.config(state='disabled')

    def host_chat(self):
        port = int(self.chat_port.get())
        self.log_chat(f"Starting Chat Server on port {port}...")
        threading.Thread(target=self._run_chat_server, args=(port,), daemon=True).start()

    def join_chat(self):
        ip = self.chat_ip.get()
        port = int(self.chat_port.get())
        self.log_chat(f"Connecting to {ip}:{port}...")
        threading.Thread(target=self._run_chat_client, args=(ip, port), daemon=True).start()

    def _run_chat_server(self, port):
        #to simple chat module file
        self.chat_socket = simple_chat.start_server_socket(port)
        self.log_chat("Client connected!")
        simple_chat.receive_messages_gui(self.chat_socket, self.log_chat)

    def _run_chat_client(self, ip, port):
        #to simple chat module file
        self.chat_socket = simple_chat.start_client_socket(ip, port)
        self.log_chat("Connected to Server!")
        simple_chat.receive_messages_gui(self.chat_socket, self.log_chat)

    def send_chat_msg(self):
        msg = self.chat_entry.get()
        if msg and self.chat_socket:
            self.log_chat(f"Me: {msg}")
            #send
            simple_chat.send_message_net(self.chat_socket, msg)
            self.chat_entry.delete(0, tk.END)

#------------------------------------------------------------------------------------------------------------------------
# module E / Settings and Errors


    def build_settings_tab(self):
        ttk.Label(self.tab_settings, text="Settings & Error Management", font=("Arial", 14, "bold")).pack(pady=10)

        frame = ttk.Frame(self.tab_settings)
        frame.pack(pady=5)

        ttk.Label(frame, text="Send Buffer (bytes):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_send = ttk.Entry(frame, width=10)
        self.entry_send.insert(0, "4096")
        self.entry_send.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Recv Buffer (bytes):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_recv = ttk.Entry(frame, width=10)
        self.entry_recv.insert(0, "4096")
        self.entry_recv.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame, text="Timeout (sec):").grid(row=0, column=4, padx=5, pady=5)
        self.entry_timeout = ttk.Entry(frame, width=10)
        self.entry_timeout.insert(0, "0.5")
        self.entry_timeout.grid(row=0, column=5, padx=5, pady=5)

        self.settings_output = scrolledtext.ScrolledText(self.tab_settings, width=80, height=15)
        self.settings_output.pack(pady=15)

        ttk.Button(self.tab_settings, text="Apply Settings & Run Error Management Test", command=self.run_settings_test).pack()

  


#------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = DaemonGUI(root)
    root.mainloop()