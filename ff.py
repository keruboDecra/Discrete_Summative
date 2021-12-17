# importing network module for generating graphs
import networkx as nx

# Importing the matplotlib module to visualize the graphs
import matplotlib.pyplot as plt

# Graph Properties
num_nodes = 10  # number of nodes

# erdos_renyi_graph is used to define the vertices and establish an independent model for the graph.
graph = nx.generators.erdos_renyi_graph(num_nodes, 0.6)

# Assigns a position to every node in the graph
pos = nx.spring_layout(graph)

# checks if graph is connected
connected = nx.is_connected(graph)

# Empty list for appending even nodes
even_degree_nodes = []

# Empty list for appending odd nodes
odd_degree_nodes = []

# loop for checking the node types if even or odd- to enable graph comparison
for node in graph.nodes:
    if graph.degree(node) != 0:
        if graph.degree(node) % 2 == 0:
            even_degree_nodes.append(node)
    elif graph.degree(node) != 0 and graph.degree(node) % 2 != 0:
        odd_degree_nodes.append(node)

if even_degree_nodes == list(graph.nodes):
    print("This is a euler circuit")
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.eulerian_circuit(graph, source=None)
    plt.show()


else:
    print(f"Is the graph connected?: {connected}")
    print(f"This is not an Euler circuit because of these odd degree nodes: {odd_degree_nodes} ")
    nx.draw_random(graph, with_labels=True)
    plt.show()  # plots graph

import time
#Estimating probability using exponential formula
print("Probability analysis...")
time.sleep(2)
no_of_trials = 10
print((no_of_trials - 1) / 2 ** no_of_trials)
