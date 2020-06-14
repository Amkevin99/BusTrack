from threading import Thread
import Global_vars
import json
import time


class Client(Thread):

    def __init__(self, connection):
        Thread.__init__(self)
        self.con = connection

    def run(self):

        client_type = json.loads(self.con.recv(1024).decode())
        print(type(client_type),client_type)

        if client_type["type"] == 1:

            Global_vars.shared ="client"
            print(Global_vars.shared)
            #passenger on server side receives coordinates from server thread and ends to client
            print("connected a passenger")
            current_position = 0
            while True:
                print("still in passenger thread")
                if Global_vars.route_progress[client_type["route"]] != current_position:
                    print(f"current position is at {current_position}")
                    Global_vars.route_progress[client_type["route"]] = current_position
                time.sleep(1)





        elif client_type["type"] == 0:
            #bus driver on server side forwards message to client thread
            print("connected a bus_driver")
            Global_vars.drivers_online = True
            Global_vars.routes_Available[client_type["route"]] = True
            self.con.send(bytes(1))

            while True:
                print("still in bus driver thread")
                location = self.con.recv(1024).decode()
                Global_vars.route_progress = location
                print(Global_vars.route_progress)
                self.con.send(bytes(1))






