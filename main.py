from count import count_spanning_trees, edge_probability
from graphs import graph_with_edge_pr_one, \
                   graph_with_edge_pr_n, \
                   graph_with_edge_pr_nk

graph = """
GRAPH
0-1-2
| | |
3-4-5
"""
print(graph)

edge_list = [ (0,1),(1,2),
              (0,3),(1,4),(2,5),
              (3,4),(4,5) ]

print("count of spanning trees (should be 15):")
print(int(round(count_spanning_trees(edge_list))))
print()

edge = (1,4)
print("probability of edge %s (should be 9/15):" % str(edge))
print("pr(edge=%s) = %.4f" % (str(edge),edge_probability(edge_list,edge)))
print()

edge = (2,5)
print("probability of edge %s (should be 11/15):" % str(edge))
print("pr(edge=%s) = %.4f" % (str(edge),edge_probability(edge_list,edge)))
print()


print("testing graph functions...")
n = 5
k = 3
edge = (0,1)

edge_list = graph_with_edge_pr_one(n,edge)
print("probability of edge %s (should be 1):" % str(edge))
print("pr(edge=%s) = %.4f" % (str(edge),edge_probability(edge_list,edge)))

edge_list = graph_with_edge_pr_n(n,edge)
print("probability of edge %s (should be %d/%d):" % (str(edge),n-1,n))
print("pr(edge=%s) = %.4f" % (str(edge),edge_probability(edge_list,edge)))

edge_list = graph_with_edge_pr_nk(n,k,edge)
print("probability of edge %s (should be %d/%d):" % (str(edge),k-1,k))
print("pr(edge=%s) = %.4f" % (str(edge),edge_probability(edge_list,edge)))
