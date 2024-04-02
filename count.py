from functools import reduce
import numpy
from numpy.linalg import det

class Graph:
    def __init__(self,edges):
        # edges is a list of edges
        # where each edge is a tuple (i,j)
        # and where i and j are integer indices of nodes, 
        # starting at index 0
        self.edges = edges
        # find the set of nodes from the edges
        self.nodes = reduce(set.union,edges,set())
        self.m = len(self.edges)   # number of edges
        self.n = max(self.nodes)+1 # number of nodes
        # construct the node-versus-edge matrix
        self.A = numpy.zeros((self.n,self.m))
        for i,(x,y) in enumerate(edges):
            self.A[x,i] = 1
            self.A[y,i] = -1

    def minus_one(self,i=0):
        # delete a row and column
        return numpy.delete(self.A,i,axis=0)

def count_spanning_trees(edge_list):
    """given a graph, as a list of edges, returns the number of
    spanning trees in the graph.  note the count is returned as a
    floating point number.

    """
    graph = Graph(edge_list)
    M = graph.minus_one()
    return det(M@M.T)

def _remove_edge(edge_list,edge):
    edge_list = list(edge_list) # make a copy
    i,j = edge
    if (i,j) in edge_list: edge_list.remove((i,j))
    if (j,i) in edge_list: edge_list.remove((j,i))
    return edge_list

def edge_probability(edge_list,edge):
    """given a graph, as a list of edges, and an edge in the list,
    returns the edge-appearance probability of the edge among all of
    the spanning trees in the given graph.  the probability is
    returned as a floating point number

    """

    edge_list_without = _remove_edge(edge_list,edge)
    count = count_spanning_trees(edge_list)
    count_without = count_spanning_trees(edge_list_without)
    count_with = count - count_without
    return count_with/count
