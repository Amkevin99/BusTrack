from threading import Thread
import Global_vars


class Client(Thread):

    def __init__(self, connection):
        Thread.__init__(self)
        self.con = connection

    def run(self):
        #print(f"hello {self.con} from the main thread")
        client_type = int(self.con.recv(1024).decode())
        #print(type(client_type),client_type)

        if client_type == 1:
            Global_vars.shared ="client"

            print(Global_vars.shared)
            #passenger on server side receives coordinates from server thread and ends to client
            print("connected a passenger")


        elif client_type == 0:
            #bus driver on server side forwards message to client thread
            print("connected a bus_driver")




