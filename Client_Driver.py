import socket
import Global_vars
from time import sleep


route = "A"
initial_massage = f'''{{ "type": 0,"route" : "{route}"}}'''
client = socket.socket()
client.connect((socket.gethostbyname(str(socket.gethostname())), 5050))
client.send(bytes(initial_massage, "utf-8"))

client.recv(1)

enroute = True
distance = 0

while distance < 10 and enroute:

    client.send(bytes(str(distance), "utf-8"))
    client.recv(1)
    sleep(1)
    distance = distance + 1




client.close()