from threading import Thread
import socket

PORT = 1488
HOST = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()

def treatment(connection):
