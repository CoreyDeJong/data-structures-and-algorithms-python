class Graph:
    
    def __init__(self):
        # adjacency list is the graph, starting as an empty list
        self._adjacency_list = {}

    def add_vertex(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):
        
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')

        edge = Edge(end_vertex, weight)

        adjacencies = self._adjacency_list[start_vertex] # list of neighbors
        
        adjacencies.append(edge)

    # gets all the keys from vertex's/nodes
    def get_vertex(self):
        return self._adjacency_list.keys()

    # neighbors are vertex/nodes that are edge/connected to each other
    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])

    
    def __len__(self):
        return len(self._adjacency_list)

# creates Vertex/Nodes
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight