# Prim's and Dijkstra's Algorithms

This repo provides an implementation of and comparison between Prim's and Dijkstra's algorithms. Both are graph optimisation algorithims, although each have slightly different implementations and uses. 


### Background

Before we look into the algorithm, we must first understand minimum spanning trees (MSTs) and the idea of a shortest path. 

## Minimum Spanning Trees

We start out with an undirected weighted graph, consisting of vertices, edges, and edge weights. A spanning tree is a subgraph that connects all the vertices of a graph. The MST is a spanning tree such that the sum of the edge weights, or the distance, is minimised. 

In this example, we start out with an undirected weighted graph. 

![OG graph](/og_graph.png)

The MST for this graph is shown below, with weight 29. Note that this MST contains every single vertex from the original graph. 

![MST](/mst.png)

## Shortest Path

We start out with a weighted graph, either directed or undirected. The shortest path between two vertices is defined as the path along the graph such that the sum of the edge weights, or the distance, is minimised. 

Using the same graph as before, we can observe that the shortest path between vertices `A` and `I` is shown below, with path length 10. 

![shortest_path](/shortest_path.png)

### Prim's and Dijkstra's Algorithms

Prim's algorithm is a greedy algorithm that finds the minimum spanning tree for an undirected weighted graph. It starts at one vertex, and adds onto that vertex by looking at the cheapest possible path to go next. It repeats this process until it has spanned the entire graph. 


Dijkstra's algorithm is an algorithm that finds the shortest path of either a directed or undirected graph. However, the graph cannot have negative edge weights. It's implementation is similiar to Prim's in takes a greedy approach. It starts at a source vertex and calculates the shortest distance from each vertex to the source. For each calculated distance, it saves the value if it finds a shorter path that the path that it had saved before. Once Dijkstra’s algorithm has found the shortest path between the source vertex and another vertex, it marks this other vertex as visited. It repeats the process until all vertices are visited. 

In the case of a weighted graph, which this implementation does not cover, the paths that Dijkstra's algorithm explores are limited by the direction of the edges.

### Implementation

Although the two algorithms return different outputs, their approach is similar due to their greedy nature. An implementation of these algorithms can be accomplished using a Min Heap. 

Prim's Algorithm
1. Create a Min Heap of size V where V is the number of vertices in the graph. Every node of the min-heap contains the vertex number and distance value of the vertex. 
2. Initialize Min Heap with source vertex as root (the distance value assigned to source vertex is 0). The distance value assigned to all other vertices is infinite. 
3. While Min Heap is not empty, do the following:
a. Extract the vertex with minimum distance value node from Min Heap. Let the extracted vertex be u. 
b. For every adjacent vertex v of u, check if v is in Min Heap. If v is in Min Heap and the distance value is more than **the weight of u-v**, then update the distance value of v.

Dijkstra's Algorithm
1. Create a Min Heap of size V where V is the number of vertices in the graph. Every node of the min-heap contains the vertex number and distance value of the vertex. 
2. Initialize Min Heap with source vertex as root (the distance value assigned to source vertex is 0). The distance value assigned to all other vertices is infinite. 
3. While Min Heap is not empty, do the following:
a. Extract the vertex with minimum distance value node from Min Heap. Let the extracted vertex be u. 
b. For every adjacent vertex v of u, check if v is in Min Heap. If v is in Min Heap and the distance value is more than **the weight of u-v plus the distance value of u**, then update the distance value of v.

Note that the only difference between these algorithm's is in the decision to update the distance value at each vertex. In the case of Prim's algorithm, we're checking to see if the distance value is more than the weight of u-v, whereas in Dijkstra's algorithm, we're checking to see if the distance value is more than the weight of u-v plus the distance of u. 


<!-- How to run algorithms -->


<!-- running time, time and space complexity -->

<!-- uses of these algorithms -->