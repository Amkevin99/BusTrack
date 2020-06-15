import socket
import sys
import time


To = "F"
Fro = "C"
initial_message = f'''{{ "type": 1,"To" : "{To}","Fro":"{Fro}"}}'''

client = socket.socket()
client.connect((socket.gethostbyname(str(socket.gethostname())), 5050))
client.send(bytes(initial_message, "utf-8"))









client.close()