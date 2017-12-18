
# %% import dependencies

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# %% read network
G=nx.read_edgelist("data/network.in",
create_using=nx.DiGraph(), nodetype=int)

# %% read larger
G=nx.read_edgelist("data/larger.in",create_using=nx.DiGraph(), nodetype=int)


# 2.1 how many directed links
# %% Q 2.1 how many edges
print(G.number_of_edges())
print(G.number_of_nodes())


# %% 2.3 indegree an outdegree distribution
indegree = G.in_degree(G)
in_vals = list(indegree.values())

outdegree = G.out_degree(G)
out_vals = list(outdegree.values())

in_values = sorted(set(indegree.values()))
in_hist = [in_vals.count(x) for x in in_values]

out_values = sorted(set(outdegree.values()))
out_hist = [out_vals.count(x) for x in out_values]

plt.loglog(in_values,in_hist,'ro')
plt.loglog(out_values,out_hist,'b*')
plt.legend(['in-degree','out-degree'])
plt.ylabel('Occurrence')
plt.title('network.in loglog degree distribution')
plt.savefig('degreeloglog.png')
plt.show()

# %% 2.4 weekly connected components
print('Weakly connected components: ',
 nx.number_weakly_connected_components(G))
print('Strongly connected components: ', nx.number_strongly_connected_components(G))

ls = max(
  nx.strongly_connected_component_subgraphs(G),
  key=len)

print('LS num of edges: ', ls.number_of_edges())
print('LS num of nodes: ', ls.number_of_nodes())


# %% 2.5

dist_hist = {}

for node in ls.nodes():
    dist_from_node = nx.single_source_shortest_path_length(ls,source=node)
    for k, v in dist_from_node.items():
        if v in dist_hist:
            dist_hist[v] += 1
        else:
            dist_hist[v] = 0

plt.bar(list(dist_hist.keys()), list(dist_hist.values()))
plt.xlabel('Distance')
plt.ylabel('Occurrence')
plt.title("Distance distribution of LSCC in network.in")
plt.savefig('distdist.png')
plt.show()
