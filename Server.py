import socket
import sys

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

    c, addr = sockt.accept()
    print("user connected")


sockt.close()
