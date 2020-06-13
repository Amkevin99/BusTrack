import socket
import sys

client = socket.socket()
client.connect((socket.gethostbyname(str(socket.gethostname())), 5050))
client.send(bytes("2", "utf-8"))


client.close()