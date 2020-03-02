from __future__ import print_function
from heapdict import heapdict

graph = [ [] for i in range(8) ]

graph[0].append(1)
graph[0].append(4)
graph[0].append(5)

graph[1].append(0)
graph[1].append(2)
graph[1].append(5)
graph[1].append(6)

graph[2].append(1)
graph[2].append(6)
graph[2].append(3)

graph[3].append(2)
graph[3].append(6)
graph[3].append(7)

graph[4].append(0)
graph[4].append(5)

graph[5].append(4)
graph[5].append(0)
graph[5].append(1)
graph[5].append(6)

graph[6].append(1)
graph[6].append(2)
graph[6].append(3)
graph[6].append(7)
graph[6].append(5)

graph[7].append(6)
graph[7].append(3)

lengthMap = {}
lengthMap[(0,1)] = 7
lengthMap[(0,4)] = 1
lengthMap[(0,5)] = 6

lengthMap[(1,2)] = 3
lengthMap[(1,6)] = 12
lengthMap[(1,5)] = 8

lengthMap[(2,3)] = 11
lengthMap[(2,6)] = 5

lengthMap[(3,6)] = 10
lengthMap[(3,7)] = 9

lengthMap[(4,5)] = 4
lengthMap[(5,6)] = 13
lengthMap[(6,7)] = 2


def prim(G, cost):
    S = set()
    T = set()

    source = 0

    cheapestEdge = [float("inf") for i in range(len(G))]
    cheapestEdge[source] = 0

    pred = [None for i in range(len(G))]

    pq = heapdict()
    for i in range(len(G)):
        pq[i] = cheapestEdge[i]

    while len(pq) != 0:
        u = pq.popitem()[0] # (vertex, priority) <- popitem() 
        S.add(u)
        T.add((pred[u], u))
        for v in G[u]:
            if v in S:
                continue
            if (u,v) in cost:
                edgeCost = cost[(u,v)]
            elif (v,u) in cost:
                edgeCost = cost[(v,u)]
            else:
                print('No edge found')
                return
            if edgeCost < cheapestEdge[v]:
                pq.__setitem__(v, edgeCost)
                cheapestEdge[v] = edgeCost
                pred[v] = u
    
    print(T)
    printEdges(pred)

def printEdges(pred):
    for i in range(1, len(pred)):
        print('(%d, %d)' %(i, pred[i]))

if __name__ == "__main__":
    prim(graph, lengthMap)



