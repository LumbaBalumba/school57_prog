import socket

HOST = "127.0.0.1"
PORT = 7788

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

s.send(b"Hello world")
