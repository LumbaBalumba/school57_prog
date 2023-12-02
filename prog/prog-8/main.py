import socket

HOST = "127.0.0.1"
PORT = 7788

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()


data = conn.recv(4096)
print(data)
