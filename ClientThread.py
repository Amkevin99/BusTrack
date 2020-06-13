from threading import Thread


class Client(Thread):

    def __init__(self, connection):
        Thread.__init__(self)
        self.con = connection

    def run(self):
        print(f"hello {self.con} from the main thread")
        client_type = int(self.con.recv(1024).decode())

        if client_type == 1:
           #passenger on server side receives coordinates from server thread and ends to client
           print("hey passenger")

        elif client_type == 0:
            #bus driver on server side forwards message to client thread
            print("hey bus_driver")
            client_type = int(self.con.recv(1024).decode())



