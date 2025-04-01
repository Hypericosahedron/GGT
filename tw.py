import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

loc = "University of Warwick, UK"
G = ox.graph_from_place(loc)
ox.plot.plot_graph(G) # visualises the graph

G = nx.Graph(G) # removes directionality and repeated edges (loops still allowed)
nx.draw(G, **{"node_size": 4})
plt.show()

tw, decomp = nx.approximation.treewidth_min_degree(G)
print(tw)