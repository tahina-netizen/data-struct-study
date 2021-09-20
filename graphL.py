"""
Unoriented graph.
Implemented using adjacency list.
"""
from typing import List


class GraphL:
    """
    Create a graph with zero vertex
    """
    def __init__(self) -> None:
        self._adjacency_list = []

    """
    Tell if this graph is null.
    A graph is null when it has zero vertex.
    :return: (bool) true iff this graph is null
    """
    def is_null(self) -> bool:
        return self._adjacency_list == []
    """
    Give the number of vertices of this graph
    :return: (int) the number of vertices of this graph
    """
    def order(self) -> int:
        return len(self._adjacency_list)

    """
    Give the degree of given vertex.
    :param vertex: (identifier) identifier of the vertex
    :return: (int) the number of neighbors of the given vertex.
    """
    def degree(self, vertex: int) -> int:
        if (vertex >= self.order()):
            raise Exception("Unknown vertex")
        return len(self._adjacency_list[vertex])

    """
    Gives a list of the vertices'identifier of this graph.
    :return: (list) a list (of int) of the vertices'identifier of this graph.
    """
    def vertices(self) -> list:
        return [x for x in range(self.order())]

    """
    Gives the number of edges of this graph
    :return: (int) the number of edges of this graph
    """
    def size(self) -> int:
        return sum (self.degree(v) for v in self.vertices()) / 2

    """
    Add a new vertex to this graph
    :return: (int) the identifier of the added vertex.
    """
    def add_vertex(self) -> int:
        self._adjacency_list.append([])
        return len(self._adjacency_list) - 1
    """
    Add an edge between the given vertices.
    :param v1: (int) id of the vertex to be bound with v2
    :param v2: (int) id of the vertex to be bound with v1
    """
    def add_edge(self, v1: int, v2: int) -> None:
        if (v1 >= self.order() or v2 >= self.order()):
            raise Exception("Unknown vertex")
        if not self.is_bound_to(v1, v2):
            self._adjacency_list[v1].append(v2)
            self._adjacency_list[v2].append(v1)
    
    """
    Give the list of the neighbors of the given vertice.
    :return: (list) the list (of int) of the neighbors of the given vertice.
    This list is sorted by the id of the vertices.
    """
    def neighbors(self, v: int) -> list:
        if (v >= self.order()):
            raise Exception("Unknown vertex")
        return sorted(self._adjacency_list[v].copy())

    """
    Tell if v1 is bound to v2
    :return: (bool) True iff v1 is bound to v2
    """
    def is_bound_to(self, v1: int, v2: int) -> bool:
        return v2 in self.neighbors(v1) or v1 in self.neighbors(v2)