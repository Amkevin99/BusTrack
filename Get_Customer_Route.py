import Global_vars


def calculate_path(route, end_point):
    distance = 0
    route_len = route.index(end_point) + 1
    for index in range(1, route_len):
        edges = Global_vars.edges[route[index - 1]]
        #print(f"edges for {route[index-1]} is {edges}")
        for i in edges:
            #print(f"if {i[0]} == {route[index]}")
            if i[0] == route[index]:
                distance += i[1]
                break

    return distance


def passenger_after_bus(routes, fro):
    selected_routes = []
    for route in routes:
        client_dist = calculate_path(Global_vars.routes[route], fro)

        if Global_vars.route_progress[route] < client_dist:
            selected_routes.append(route)
    return selected_routes


def check_if_available(routes):
    available_routes = []
    for route in routes:
        if Global_vars.routes_Available[route]:
            available_routes.append(route)
    return available_routes


def check_routes(to, fro):
    common_routes = []
    for route in Global_vars.routes:
        if to in Global_vars.routes[route]:
            if fro in Global_vars.routes[route]:
                common_routes.append(route)
    common_routes = check_if_available(common_routes)
    return common_routes


def get_routes(to, fro):

    possible_routes = check_routes(to, fro)  # returns list of possible routes
    variable_to_track = passenger_after_bus(possible_routes, fro)
    return variable_to_track
