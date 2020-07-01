## collaborated with multiple team members to complete this assignment and testing
from graphs import *

def get_edge(graph, city_list):
    cost = 0
    for i in range(1, len(city_list)):
        start_city = (city_list[i-1])
        end_city = (city_list[i])
        neighbors = graph.get_neighbors(start_city)
        print("Corey", neighbors)
        are_neighbors = False

        for neighbor in neighbors:
            if end_city == neighbor.vertex.value:
                cost += neighbor.weight
                are_neighbors = True
                break

    if are_neighbors == False:
        return [False, '$0']

    else:
        return [True, f'${cost}']        