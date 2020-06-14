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
        #print(type(client_type), client_type)

        if client_type["type"] == 1:

            Global_vars.shared ="client"
            #print(Global_vars.shared)
            #passenger on server side receives coordinates from server thread and ends to client
            print("connected a passenger")
            current_position = Global_vars.route_progress[client_type["route"]]
            while True:
                if not Global_vars.arrived:
                    print("still in passenger thread")
                    if Global_vars.route_progress[f'{client_type["route"]}'] != current_position:
                        print(f"current position is at {current_position}")
                        current_position = Global_vars.route_progress[client_type["route"]]
                    time.sleep(2)
                else:
                    print("Now Arrived")
                    break

            self.con.close()






        elif client_type["type"] == 0:
            #bus driver on server side forwards message to client thread
            print("connected a bus_driver")
            Global_vars.drivers_online = True
            Global_vars.routes_Available[client_type["route"]] = True
            self.con.send(bytes(1))

            while True:
                print("still in bus driver thread")
                location = self.con.recv(1024).decode()
                Global_vars.route_progress[f'{client_type["route"]}'] = location
                print(Global_vars.route_progress[f'{client_type["route"]}'])
                self.con.send(bytes(1))

                progress = int(self.con.recv(1).decode())
                print(f"[BROADCASTING] Driver is still in enroute")
                if progress == 0:
                    print("bus thread should be active")
                    self.con.send(bytes(1))
                else:
                    Global_vars.arrived = True
                    break
            self.con.close()






