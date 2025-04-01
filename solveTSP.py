# This program takes input of a location and builds a csv file containing coordinates of an approximate solution to the corresponding TSP problem

import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from pprint import pprint

loc = input("Enter location: ")

G = ox.graph.graph_from_place(loc)
# G = nx.Graph(G)
print("Graph done")


map = {}
nodes = []
i = 0
for node in G.nodes:
    map[node] = i
    nodes.append(i)
    i += 1



pos = []
for _ in range(len(nodes)):
    pos.append(0)
for key in G._node:
    pos[map[key]] = ((G._node[key]["x"], G._node[key]["y"]))

edges = []
for e in G.edges:
    edges.append((map[e[0]], map[e[1]]))

print("Nodes, edges, pos done")

H = nx.Graph()
H.add_edges_from(edges)

R = nx.algorithms.approximation.traveling_salesman_problem(H)
# print(R)
print("TSP done")

fn = loc.split(",")[0]+".csv"
with open(fn, "w") as f:
    f.write("x,y\n")
    for r in R:
        f.write(str(pos[r][0]) + "," + str(pos[r][1]) + "\n")


options = {
    "node_size": 10
}

# fig, ax = ox.plot.plot_graph(G)
# plt.show()
# nx.draw(H, pos=pos, **options)
# plt.show()