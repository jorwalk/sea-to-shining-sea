"""Simple Traveling salesman problem between cities."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

from src.data import Data

def create_data_model(depot):
    """Stores the data for the problem."""
    data = Data()
    data.distance()

    obj = {}
    obj['distance_matrix'] = data.matrix
    obj['num_vehicles'] = 1
    obj['depot'] = depot
    return obj

def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    data = Data()
    cities = []
    route = []

    index = routing.Start(0)

    route_distance = 0
    while not routing.IsEnd(index):
        cities.append( data.capital_name(manager.IndexToNode(index)) )
        route.append(manager.IndexToNode(index))

        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)

    cities.append(data.capital_name(manager.IndexToNode(index)))
    route.append(manager.IndexToNode(index))

    return cities, route


def main(depot):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(depot)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if assignment:
        return print_solution(manager, routing, assignment)