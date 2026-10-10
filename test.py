import socket
name = socket.gethostname()
print(socket.gethostbyname_ex(name)[2])