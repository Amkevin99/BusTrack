import socket
import sys
import time


route = "A"
initial_massage = f'''{{ "type": 1,"route" : "{route}"}}'''
client = socket.socket()
client.connect((socket.gethostbyname(str(socket.gethostname())), 5050))
client.send(bytes(initial_massage, "utf-8"))

while True:
    client.recv(1)








client.close()