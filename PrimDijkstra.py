import Heap
import math
INF = math.inf

def PrimDijkstra(graph, start, alg):
        """ Takes a graph, start vertex, and alg 'D' or 'P', and runs
        either Prim or Dijkstra from the start vertex, returning an
        adjacency list of the tree, represented as a directed graph
        with edges emanating from the start vertex. """
        h = Heap.Heap(len(graph))

        # populate heap
        for i in range(len(graph)):
                if i is not start:
                        h.insert(Heap.Item(INF, i))
        h.insert(Heap.Item(0, start))

        # populate index
        output = [[] for i in range(len(graph))]
        locked = []
        while h.elements is not 0:
                minElement = h.deleteMin()
                minValue = minElement.value
                minVertex = minElement.vertex
                locked.append(minVertex)
                for element in graph[minVertex]:
                        if element[0] not in locked:
                                if alg == 'P':
                                        offer = element[1]
                                else:
                                        offer = element[1] + minValue 
                                h.decreaseKey(element[0], offer, minElement)
                if minElement.predecessor:
                        output[minElement.predecessor.vertex] += [minVertex]
        return output


def navigate(graph, start, end):
        """ Takes a graph, start vertex, and end vertex as input and returns
        a list representing a shortest path from the start vertex to the
        end vertex in that graph. """
        tree = PrimDijkstra(graph, start, "D")
        pathD = {}
        # BFS 
        if start == end:
                return [start]
        queue = []
        queue.append(start)
        visited = [False] * (len(graph)) 
        visited[start] = True
        pathD[start] = [start]
        while queue:
                current = queue.pop(0)
                for vertex in tree[current]:
                        if vertex == end: 
                                return pathD[current] + [vertex]
                        elif not visited[vertex]:
                                queue.append(vertex)
                                visited[vertex] = True
                                pathD[vertex] = pathD[current] + [vertex]
        return []