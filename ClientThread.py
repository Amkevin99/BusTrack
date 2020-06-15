import Get_Customer_Route
from threading import Thread
import Global_vars
import json
import time


class Client(Thread):

    def __init__(self, connection):
        Thread.__init__(self)
        self.con = connection

    def run(self):
        # Receive first initial message with connection details in for of a
        # json object - { type -> passenger type (driver = 0 ,passenger = 1) , route -> current route }
        client_type = json.loads(self.con.recv(1024).decode())

        if client_type["type"] == 1:
            # PASSENGER THREAD LOGIC
            # passenger on server side fetches updated coordinates from server for specific route and sends to client
            print("    [REGISTERING CLIENT] connected a passenger")
            route = ["RA"]#Get_Customer_Route.get_routes(client_type["To"], client_type["Fro"])

            current_position = 0

            while True:
                # Runs until [arrived] is set to false meaning bus is still on its way
                if not Global_vars.arrived:
                    print("    [FETCHING COORDINATES] passenger is fetching current coordinates")

                    # Checks whether coordinates have been updated by bus driver
                    # if they have proceeds to update the client
                    for bus in route:
                        if Global_vars.route_progress[bus] != current_position:
                            current_position = Global_vars.route_progress[bus]
                            print(f"    [UPDATED COORDINATES] new position is at (({current_position}))")
                    time.sleep(2)
                else:
                    print("    [NOW ARRIVED]")
                    Global_vars.arrived = False
                    break

        elif client_type["type"] == 0:
            # DRIVER THREAD LOGIC
            # Driver thread on server side receives bus coordinates for specific route and
            # updates the global progress variable which will then be consumed by the passenger

            print("[[REGISTERING CLIENT]] connected a bus driver \n")

            Global_vars.drivers_online = True
            Global_vars.routes_Available[client_type["route"]] = True

            # Bus Driver can only communicate with client after getting an acknowledgement
            # from the server hence the next line of code would signal that the thread is now
            # ready to receive coordinates from the server
            self.con.send(bytes(1))

            while True:
                print("[[RECEIVING COORDINATES]] server is waiting for current coordinates")
                location = int(self.con.recv(1024).decode())
                # Update Global route progress with transmitted location
                # i.e  f'{client_type["route"]}' should return route type eg A in the form  of a string
                # this in turn is used to query the route progress dictionary
                Global_vars.route_progress[f'{client_type["route"]}'] = location

                print(f'[[UPDATING COORDINATES]] updated with {location}')
                # Acknowledgement receipt of location by server is sent to driver
                # so it can continue broadcasting location
                self.con.send(bytes(1))

                # this next message will determine if the bus has arrived or is still on its way ,
                # if its still on its way the server will request for more information until arrived
                # otherwise it will stop requesting for information
                arrived = int(self.con.recv(1).decode())

                if arrived == 0:
                    print(f"[[BROADCASTING]] Driver is still in enroute \n")
                    self.con.send(bytes(1))
                else:
                    Global_vars.arrived = True
                    print(f"[[AT DESTINATION]] Driver Has now arrived at destination \n")
                    Global_vars.drivers_online = False
                    Global_vars.routes_Available[client_type["route"]] = False
                    Global_vars.route_progress[client_type["route"]] = None

                    break

            # Close Connection and join Thread clearing  the current state of
            # locations and other relevant global variables

        self.con.close()








