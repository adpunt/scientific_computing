# Prim's and Dijkstra's Algorithms

An implementation of Prim's and Dijkstra's algorithms. Both are graph optimisation algorithims, although each have slightly different implementations and uses. 


## Background

Before we look into the algorithm, we must first understand minimum spanning trees (MSTs) and the idea of a shortest path. 

### Minimum Spanning Trees

We start out with an undirected weighted graph, consisting of vertices, edges, and edge weights. A spanning tree is a subgraph that connects all the vertices of a graph. The MST is a spanning tree such that the sum of the edge weights, or the distance, is minimised. 

In this example, we start out with the following directed weighted graph. 

![OG graph](/og_graph_directed.png)

The MST for this graph is shown below, with weight 19. Note that this MST contains every single vertex from the original graph and all edges were considered undirected.

![MST](/min_spanning_tree.png)

### Shortest Path

We start out with a weighted graph, either directed or undirected. The shortest path between two vertices is defined as the path along the graph such that the sum of the edge weights, or the distance, is minimised. 

Using the same graph as before, we can observe that the shortest path between vertices `1` and `4` is shown below, with path length 14.

![shortest_path](/shortest_path_1_4.png)

## Prim's and Dijkstra's Algorithms

Prim's algorithm is a greedy algorithm that finds the minimum spanning tree for an undirected weighted graph. It starts at one vertex, and adds onto that vertex by looking at the cheapest possible path to go next. It repeats this process until it has spanned the entire graph. 


Dijkstra's algorithm is an algorithm that finds the shortest path of a directed graph. However, the graph cannot have negative edge weights. It's implementation is similiar to Prim's such that it takes a greedy approach. It starts at a source vertex and calculates the shortest distance from each vertex to the source. For each calculated distance, it saves the value if it finds a shorter path that the path that it had saved before. Once Dijkstra’s algorithm has found the shortest path between the source vertex and another vertex, it marks this other vertex as visited. It repeats the process until all vertices are visited. 


### Implementation

Although the two algorithms return different outputs, their approach is similar due to their greedy nature. An implementation of these algorithms can be accomplished using a Min Heap. 

Prim's Algorithm
1. Create a Min Heap of size V where V is the number of vertices in the graph. Every node of the min-heap contains the vertex number and distance value of the vertex. 
2. Initialize Min Heap with source vertex as root (the distance value assigned to source vertex is 0). The distance value assigned to all other vertices is infinite. 
3. While Min Heap is not empty, do the following:
    1. Extract the vertex with minimum distance value node from Min Heap. Let the extracted vertex be u. 
    2. For every adjacent vertex v of u, check if v is in Min Heap. If v is in Min Heap and the distance value is more than **the weight of u-v**, then update the distance value of v.

Dijkstra's Algorithm
1. Create a Min Heap of size V where V is the number of vertices in the graph. Every node of the min-heap contains the vertex number and distance value of the vertex. 
2. Initialize Min Heap with source vertex as root (the distance value assigned to source vertex is 0). The distance value assigned to all other vertices is infinite. 
3. While Min Heap is not empty, do the following:
    1. Extract the vertex with minimum distance value node from Min Heap. Let the extracted vertex be u. 
    2. For every adjacent vertex v of u, check if v is in Min Heap. If v is in Min Heap and the distance value is more than **the weight of u-v plus the distance value of u**, then update the distance value of v.

Note that the only difference between these algorithms is in the decision to update the distance value in the Min Heap at each vertex. In the case of Prim's algorithm, we're checking to see if the distance value is more than the weight of u-v, whereas in Dijkstra's algorithm, we're checking to see if the distance value is more than the weight of u-v plus the distance of u. 

## Running Code

To run this code download the repo and execute the `PrimDijkstra.py` script from the command line
```
git clone https://github.com/adpunt/scientific_computing.git
python -i PrimDijkstra.py
```

Now, you want to define your graph. The graph should be in the form of an adjaceny list. Each inner list represents a vertex with it's adjacent vertices and edge weights. These adjacent vertices and edge weights should be in the form of tuples with the structure `(<adjacent_vertex>, <edge_weight>)`. This graph will be directed. However, if you choose to use Prim's algorithm, it will be considered undirected. 

For example, the graph from above would have the following structure:
```
graph = [ [],
           [(2, 4), (6, 2)],
           [(1, 4), (6, 3), (5, 4), (3, 7)],
           [(2, 7), (5, 4), (4, 9)],
           [(3, 9), (5, 6)],
           [(6, 8), (2, 4), (3, 4), (4, 6)],
           [(1, 2), (2, 3), (5, 8)]]
```

Note that first `[]` index represents that vertex `0`, as represented by the graph above.

Once your graph is defined, you can choose to run either Prim's algorithm to find the MST of the undirected version of the graph, or Dijkstra's algorithm to find the shortest path of the directed version of the graph.

To run Prim's algorithm, call `PrimDijkstra(<graph>, <start_vertex>, 'P')`. This will return an adjaceny list of the minimum spanning tree, represented as a graph with edges emanating from the start vertex. 

To run Dijkstra's algorithm, either call `PrimDijkstra(<graph>, <start_vertex>, 'D')`, which will return a shortest path tree emanating from the start vertex, or `navigate(<graph>, <start_vertex>, <end_vertex>`, which will return the shortest path between the start and end vertices. 


## Complexity
Due to the similar nature of the implementation, the time complexity of these algorithms is the same. 

For a graph with `V` vertices and `E` edges, for each vertex, we find the adjacent vertex with the shortest edge weight. This operation is just a linear search of the adjacency matrix, taking `O(E)` time. Updating distance value of this adjacent vertex would seemingly take `O(V)` time. If these algorithms were implemented with only adjacency matrices, this would be the case. However, due to the strucutre of the Min Heap, we can complete this operation in only `O(logV)` time. This leaves us with a time complexity of `O(E*log(V))`. 


## Applications

These two algorithms have many real-world applications. 

Prim's Algorithm, or any algorithm involved in the calculation of MSTs, can be used in network design. Such networks include computer networks, transportation networks, water supply networks, electrical grids, irrigation channels, fibre-optic grids, and so on. MSTs even have applications in biology; they are used in [molecular epidemiology research to estimate relationships among individual strains or isolates](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187300/).


Dijkstra's Algorithm, or any algorithm involving in the calculation of shortest paths, can be used in mapping. An obvious example is finding the least possible geographical distance on a map, useful for tools like Google Maps. It can also be used in telephone networks, where it can decrease the obstacles taken place for transmission. Shortest path algorithms also have applications in biology, where they can be used to [count the number of shortest paths between pairs of genes in biological networks](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2480-z).

