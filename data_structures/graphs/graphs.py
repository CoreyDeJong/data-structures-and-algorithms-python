## collaborated with multiple team members to complete this assignment and testing

from stacks_and_queues import Queue


# enqueue = Queue.enqueue()
# dequeue = Queue.dequeue()




class Graph:
    
    def __init__(self):
        # adjacency list is the graph, starting as an empty list
        self._adjacency_list = {}



    def add_vertex(self, value):
        v = Vertex(value)
        self._adjacency_list[v.value] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):
        
        if start_vertex.value not in self._adjacency_list:
            raise KeyError('Start Vertex not in graph')

        if end_vertex.value not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')

        edge = Edge(end_vertex, weight)

        adjacencies = self._adjacency_list[start_vertex.value] # list of neighbors
        
        adjacencies.append(edge)


        edge2 = Edge(start_vertex, weight)
        adjacencies = self._adjacency_list[end_vertex.value] # list of neighbors
        
        adjacencies.append(edge2)


    # gets all the keys from vertex's/nodes
    def get_vertex(self):
        return self._adjacency_list.keys()

    # neighbors are vertex/nodes that are edge/connected to each other
    def get_neighbors(self, vertex):
        # return self._adjacency_list.get(vertex, [])
        return self._adjacency_list[vertex]

    
    def __len__(self):
        return len(self._adjacency_list)




    def breadth_first(self, vertex):
        nodes = []
        breadth = Queue()
        breadth.enqueue(vertex)
        # vertex.visited=True

        while breadth.front:
            front_node = breadth.dequeue()
            if front_node.visited == False: 
                nodes.append(front_node.value)
                front_node.visited = True
            
                for edge in self.get_neighbors(front_node):
                    if edge.vertex.visited == False:
                        breadth.enqueue(edge.vertex)
        
        return nodes


# creates Vertex/Nodes
class Vertex:
    def __init__(self, value):
        self.value = value
        self.visited = False
    
    # def __str__(self):
    #     return self.value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


# g = Graph()

# pandora = g.add_vertex('pandora')
# arendalle = g.add_vertex('arendalle')
# narnia = g.add_vertex('narnia')
# naboo = g.add_vertex('naboo')

# g.add_edge(pandora, arendalle)
# g.add_edge(arendalle, narnia)
# g.add_edge(arendalle,naboo)
# g.add_edge(narnia, naboo)

# actual = g.breadth_first(pandora)
# print(actual)
