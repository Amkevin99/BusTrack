import ClientThread
import socket
import sys
import Global_vars

try:
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    print("socket created")
except socket.error as err:
    print(f"failed to create socket , reason {err}")
    sys.exit()
try:
    sockt.bind((socket.gethostbyname(str(socket.gethostname())), 5050))

except socket.error as err:
    print(f"failed bind , reason {err}")
    sys.exit()

sockt.listen(1)
print("[LISTENING] server is listening")

while True:

    client_soc, address = sockt.accept()
    print("[CONNECTING] Establishing Connection")
    new_con = ClientThread.Client(client_soc)
    print(Global_vars.shared, Global_vars.shared)
    new_con.start()
    new_con.join()
    print(Global_vars.shared)

sockt.close()
