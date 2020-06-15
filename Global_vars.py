

drivers_online = False

arrived = False

routes = {

    "RA": ["A", "B", "C", "D", "E", "F"],
    "RB": ["A", "D", "G", "E"],
    "RC": ["A", "C", "E", "F"],
    "RD": ["A", "B", "D", "E", "F"]

}

edges = {
         "A": [["B", 30], ["D", 40], ["C", 25]],
         "B": [["A", 30], ["D", 35]],
         "C": [["A", 25], ["E", 20]],
         "D": [["B", 35], ["E", 15], ["A", 40], ["G", 50]],
         "E": [["F", 10], ["D", 15], ["C", 20], ["G", 15]],
         "F": [["E", 10]],
         "G": [["D", 50], ["E", 15]]
         }

routes_Available = {
    "RA": False,
    "RB": False,
    "RC": False,
    "RD": False
}

route_progress = {

    "RA": None,
    "RB": None,
    "RC": None,
    "RD": None

}


