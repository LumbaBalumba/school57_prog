import socket
from multiprocessing import Process

PORT = 2226
HOST = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(True)
s.bind((HOST, PORT))
s.listen()


def treatment(connection, address):
    while True:
        try:
            data = connection.recv(512)
            if not data:
                exit(0)
            print(address, data)
        except Exception:
            exit(1)


conn, addr = s.accept()
while True:
    process = Process(target=treatment, args=(conn, addr), daemon=False)
    process.start()
    conn, addr = s.accept()
