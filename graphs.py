from count import count_spanning_trees, edge_probability

def graph_with_edge_pr_one(n, edge):
    """
    Returns a graph (as an edge list) where the edge-probability of the given edge is one.
    
    Parameters:
        n (int): An integer >= 3, number of nodes in the graph.
        edge (tuple): A pair (i, j) where i and j are node indices, 0 <= i, j < n.
    
    Returns:
        list: Edge list representing the graph.
    """
    edge_list = []
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) == edge or (j, i) == edge:
                edge_list.append(edge)
            else:
                edge_list.append((i, j))
    return edge_list

def graph_with_edge_pr_n(n, edge):
    """
    Returns a graph (as an edge list) where the edge-probability of the given edge is 1/n.
    
    Parameters:
        n (int): An integer >= 3, number of nodes in the graph.
        edge (tuple): A pair (i, j) where i and j are node indices, 0 <= i, j < n.
    
    Returns:
        list: Edge list representing the graph.
    """
    edge_list = []
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) == edge or (j, i) == edge:
                edge_list.append(edge)
            else:
                edge_list.append((i, j))
    pr_edge = 1.0 / n
    for i in range(len(edge_list)):
        if edge_list[i] == edge:
            edge_list[i] = (edge[0], edge[1], pr_edge)
        else:
            edge_list[i] = (edge_list[i][0], edge_list[i][1], 1 - pr_edge)
    return edge_list

def graph_with_edge_pr_nk(n, k, edge):
    """
    Returns a graph (as an edge list) where the edge-probability of the given edge is 1/k.
    
    Parameters:
        n (int): An integer >= 3, number of nodes in the graph.
        k (int): An integer 3 <= k <= n.
        edge (tuple): A pair (i, j) where i and j are node indices, 0 <= i, j < n.
    
    Returns:
        list: Edge list representing the graph.
    """
    edge_list = []
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) == edge or (j, i) == edge:
                edge_list.append(edge)
            else:
                edge_list.append((i, j))
    pr_edge = 1.0 / k
    for i in range(len(edge_list)):
        if edge_list[i] == edge:
            edge_list[i] = (edge[0], edge[1], pr_edge)
        else:
            edge_list[i] = (edge_list[i][0], edge_list[i][1], 1 - pr_edge)
    return edge_list