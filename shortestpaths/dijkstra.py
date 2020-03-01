from __future__ import print_function
from heapdict import heapdict

graph = [ [] for i in range(6) ]

graph[0].append(1)
graph[0].append(4)
graph[0].append(3)

graph[1].append(2)

graph[3].append(4)

graph[4].append(1)
graph[4].append(5)

graph[5].append(2)
graph[5].append(1)

lengthMap = {}
lengthMap[(0,1)] = 16
lengthMap[(0,4)] = 8
lengthMap[(0,3)] = 4
lengthMap[(1,2)] = 2
lengthMap[(3,4)] = 3
lengthMap[(4,1)] = 7
lengthMap[(4,5)] = 1
lengthMap[(5,2)] = 6
lengthMap[(5,1)] = 5

def dikjstra(edges, source, lengths):
    pred = [None for i in range(len(graph))]
    distance = [float("inf") for i in range(len(graph))]
    distance[source] = 0
    pq = heapdict()

    for i in range(len(graph)):
        pq[i] = distance[i]
    
    while len(pq) != 0:
        u = pq.popitem()[0] # (vertex, smallest distance) <- popitem
        
        for edge in graph[u]:
            if not edge: # no outgoing edges
                continue
            currentDistance = distance[u] + lengths[(u, edge)]
            if currentDistance < distance[edge]:
                pq.__setitem__(edge, currentDistance)
                distance[edge] = currentDistance
                pred[edge] = u
    
    printPaths(pred, 5)
    printPaths(pred, 4)
    printPaths(pred, 3)
    printPaths(pred, 2)
    printPaths(pred, 1)
    printPaths(pred, 0)
    

def printPaths(pred, i):
    while True:
        if pred[i] == None:
            print(i)    
            break
        print('%d->' % i, end='')
        i = pred[i]
    

if __name__ == "__main__":
    dikjstra(graph, 0, lengthMap)
