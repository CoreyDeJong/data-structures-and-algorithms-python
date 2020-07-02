## collaborated and code with multiple team members to complete this assignment and testing

import pytest

from graphs import *
from get_edge import *

# def test_add_vertex():

#     g = Graph()

#     expected = 'spam'

#     vertex = g.add_vertex('spam')

#     actual = vertex.value

#     assert actual == expected

# def test_add_edge():

#     g = Graph()

#     apples = g.add_vertex('apples')

#     bananas = g.add_vertex('bananas')

#     g.add_edge(apples, bananas)

#     assert True, 'Will be fully exercised in get_neighbors tests'

# def test_add_edge_interloper():

#     g = Graph()

#     insider = g.add_vertex('insider')

#     outsider = Vertex('outsider')

#     with pytest.raises(KeyError):
#         g.add_edge(outsider, insider)


# def test_get_vertices():
    
#     g = Graph()

#     apples = g.add_vertex('apples')

#     bananas = g.add_vertex('bananas')

#     actual = g.get_vertex()

#     assert len(actual) == 2


# def test_get_neighbors():
    
#     g = Graph()

#     apple = g.add_vertex('apple')

#     banana = g.add_vertex('banana')

#     g.add_edge(apple, banana)

#     neighbors = g.get_neighbors(apple)

#     assert len(neighbors) == 1

#     neighbor = neighbors[0]

#     assert neighbor.vertex.value == 'banana'

#     assert neighbor.weight == 1


# def test_get_size():

#     g = Graph()

#     apple = g.add_vertex('apple')

#     banana = g.add_vertex('banana')

#     assert len(g) == 2



###### Code 36 : Breadth First #########
# def test_breadth1():
#     g = Graph()

#     pandora = g.add_vertex('pandora')
#     arendalle = g.add_vertex('arendalle')
#     narnia = g.add_vertex('narnia')
#     naboo = g.add_vertex('naboo')

#     g.add_edge(pandora, arendalle)
#     g.add_edge(arendalle, narnia)
#     g.add_edge(arendalle,naboo)
#     g.add_edge(narnia, naboo)

#     actual = g.breadth_first(pandora)
#     expected = ['pandora', 'arendalle', 'narnia', 'naboo']
#     assert actual == expected

# def test_breadth2():
#     g = Graph()

#     narnia = g.add_vertex('narnia')
#     naboo = g.add_vertex('naboo')
#     arendalle = g.add_vertex('arendalle')
#     pandora = g.add_vertex('pandora')

#     g.add_edge(narnia, naboo)
#     g.add_edge(narnia, arendalle)
#     g.add_edge(naboo, arendalle)
#     g.add_edge(arendalle,pandora)
   
#     actual = g.breadth_first(narnia)
#     expected = ['narnia', 'naboo', 'arendalle','pandora']
#     assert actual == expected

# def test_breadth_island():
#     g = Graph()

#     pandora = g.add_vertex('pandora')
#     arendalle = g.add_vertex('arendalle')
#     narnia = g.add_vertex('narnia')
#     naboo = g.add_vertex('naboo')

#     # g.add_edge(pandora, arendalle)
#     g.add_edge(arendalle, narnia)
#     g.add_edge(arendalle,naboo)
#     g.add_edge(narnia, naboo)

#     actual = g.breadth_first(pandora)
#     expected = ['pandora']
#     assert actual == expected


############### Code 37 #################

class Test_Tester:
    def __init__(self):
        self.maps = Graph()
        self.pandora = self.maps.add_vertex('Pandora')
        self.arendelle = self.maps.add_vertex('Arendelle')
        self.metroville = self.maps.add_vertex('Metroville')
        self.monstroplolis = self.maps.add_vertex('Monstroplolis')
        self.narnia = self.maps.add_vertex('Narnia')
        self.naboo = self.maps.add_vertex('Naboo')

    def build_edges(self):
        self.maps.add_edge(self.pandora,self.arendelle, 150)
        self.maps.add_edge(self.pandora, self.metroville, 82)
        self.maps.add_edge(self.arendelle,self.metroville, 99)
        self.maps.add_edge(self.arendelle,self.monstroplolis, 42)
        self.maps.add_edge(self.metroville, self.narnia, 37)
        self.maps.add_edge(self.metroville, self.naboo, 26)
        self.maps.add_edge(self.metroville,self.monstroplolis, 105)
        self.maps.add_edge(self.monstroplolis,self.naboo, 73)
        self.maps.add_edge(self.narnia,self.naboo, 250)
        return self.maps


def test_edge_1():
    test = Test_Tester()
    maps = test.build_edges()
    expected = [True, '$82']
    actual = get_edge(maps, ['Pandora','Metroville'])
    assert actual == expected


def test_edge_2():
    test = Test_Tester()
    maps = test.build_edges()
    expected = [True, '$115']
    actual = get_edge(maps, ['Arendelle', 'Monstroplolis', 'Naboo'])
    assert actual == expected


def test_edge_3():
    test = Test_Tester()
    maps = test.build_edges()
    expected = [False, '$0']
    actual = get_edge(maps, ['Naboo', 'Pandora'])
    assert actual == expected


def test_edge_4():
    test = Test_Tester()
    maps = test.build_edges()
    expected = [False, '$0']
    actual = get_edge(maps, ['Narnia', 'Arendelle', 'Naboo'])
    assert actual == expected





###### Code 38 : Depth First #########
def test_depth1():
    g = Graph()

    A = g.add_vertex('A')
    B = g.add_vertex('B')
    C = g.add_vertex('C')
    D = g.add_vertex('D')
    G = g.add_vertex('G')

    g.add_edge(A,B)
    g.add_edge(B,D)
    g.add_edge(A,D)
    g.add_edge(B,C)
    g.add_edge(C,G)

    actual = g.depth_first('A')
    expected = ['A','B','D','C','G']
    assert actual == expected

def test_depth2():
    g = Graph()

    A = g.add_vertex('A')
    B = g.add_vertex('B')
    C = g.add_vertex('C')
    D = g.add_vertex('D')
    G = g.add_vertex('G')

    g.add_edge(A,B)
    g.add_edge(B,D)
    g.add_edge(A,D)
    g.add_edge(B,C)
    g.add_edge(C,G)

    actual = g.depth_first('G')
    expected = ['G','C','B','A','D']
    assert actual == expected

def test_depth3():
    g = Graph()

    A = g.add_vertex('A')
    B = g.add_vertex('B')
    C = g.add_vertex('C')
    D = g.add_vertex('D')
    G = g.add_vertex('G')

    g.add_edge(A,B)
    g.add_edge(B,D)
    g.add_edge(A,D)
    g.add_edge(B,C)
 

    actual = g.depth_first('G')
    expected = ['G']
    assert actual == expected