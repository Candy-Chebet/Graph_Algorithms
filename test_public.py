from count import count_spanning_trees, edge_probability
from graphs import graph_with_edge_pr_one, \
                   graph_with_edge_pr_n, \
                   graph_with_edge_pr_nk

def test_01():
    n = 5
    edge = (0,1)
    eps = 0.01 # error threshold

    edge_list = graph_with_edge_pr_one(n,edge)
    assert len(edge_list) > 0
    pr_edge = edge_probability(edge_list,edge)
    assert 1.0-eps <= pr_edge <= 1.0+eps

def test_02():
    n = 5
    edge = (0,1)
    eps = 0.01 # error threshold

    edge_list = graph_with_edge_pr_n(n,edge)
    assert len(edge_list) > 0
    pr_edge = edge_probability(edge_list,edge)
    assert (n-1.0)/n-eps <= pr_edge <= (n-1.0)/n+eps

def test_03():
    n = 5
    k = 3
    edge = (0,1)
    eps = 0.01 # error threshold

    edge_list = graph_with_edge_pr_nk(n,k,edge)
    assert len(edge_list) > 0
    pr_edge = edge_probability(edge_list,edge)
    assert (k-1.0)/k-eps <= pr_edge <= (k-1.0)/k+eps

def test_04():
    n = 5
    k = 5
    edge = (0,1)
    eps = 0.01 # error threshold

    edge_list = graph_with_edge_pr_nk(n,k,edge)
    assert len(edge_list) > 0
    pr_edge = edge_probability(edge_list,edge)
    assert (k-1.0)/k-eps <= pr_edge <= (k-1.0)/k+eps

def test_05():
    n = 16
    k = 8
    edge = (1,0)
    eps = 0.01 # error threshold

    edge_list = graph_with_edge_pr_nk(n,k,edge)
    assert len(edge_list) > 0
    pr_edge = edge_probability(edge_list,edge)
    assert (k-1.0)/k-eps <= pr_edge <= (k-1.0)/k+eps
