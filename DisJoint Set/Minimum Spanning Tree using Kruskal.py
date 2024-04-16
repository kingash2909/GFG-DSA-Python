
'''
 *  ith value in GRAPH LIST contains information between the node connected to it and weight between them.
 *  Example. for a value 2 3 1, Node 2 and Node 3 has weight 1. adj[2] = {3,1} and adj[3] = {2,1}.
 *  V -> number of nodes
 *  E -> total number of edges
 *  return the mst value
 *
 '''


def findRoot(i, parent):
    if parent[i] != i:
        parent[i] = findRoot(parent[i], parent)
    return parent[i]

# Function to perform union operation using DSU
def union(a, b, parent, rank):
    root_a = findRoot(a, parent)
    root_b = findRoot(b, parent)
    
    if root_a != root_b:
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1
            
#Function to find the minimum spanning tree value using Kruskal.
def kruskalDSU(graph,V,E):
    #code here
    graph.sort(key=lambda x: x[2])
    
    parent = [i for i in range(V)]
    rank = [0] * V
    mst_value = 0
    
    # Iterate through all edges in the sorted order
    for src, dest, weight in graph:
        # Check if adding the current edge creates a cycle
        if findRoot(src, parent) != findRoot(dest, parent):
            # If not, add the edge to the MST and update DSU
            mst_value += weight
            union(src, dest, parent, rank)
    
    return mst_value