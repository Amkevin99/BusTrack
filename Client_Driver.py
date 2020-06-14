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

while distance <= 20 and enroute:

    client.send(bytes(str(distance), "utf-8"))
    print("waiting for handshake")
    client.recv(1)
    sleep(1)
    distance = distance + 1
    print(f"distance is {distance}")
    if distance == 20:
        client.send(bytes("1", "utf-8"))
        print(f"sending a terminate cause distance is {distance}")
    else:
        client.send(bytes("0", "utf-8"))
        print(f"sending a continue cause distance is {distance}")


client.close()