import heapq
from psim import PSim
comm = PSim(5)

#each process should get a dictionary item
adj = {}  #the adjacency dictionary-list
adj['a'] = [('b', 10), ('c', 3)]
adj['b'] = [('c', 1), ('d', 2)]
adj['c'] = [('b', 4), ('d', 8), ('e', 2)]
adj['d'] = [('e', 7)]
adj['e'] = [('d', 9)]

d = {}  #tells us the weight at any node
Q = []  #used by the heapq
S = []  #big s
V = ['a', 'b', 'c', 'd', 'e']  #all the vertices

for v in V:  #assign all nodes with value infinity which is represented as 1000
    d[v] = 1000
    heapq.heappush(Q, (1000, v))

d['a'] = 0  #start is 0
heapq.heapreplace(Q, (0, 'a'))  #start is 0 on the heapq

while len(Q) != 0:
    u = heapq.heappop(Q)[1]  #this will just give us the vertex name in the tuple (0, 'a')
                             #after a heappop we need to let all the other processes know
    #print u
    S.append(u)  #put u in big S
    for v in adj[u]:  #for all the neighbors of the minimum node u  #v looks like ('b', 10)
        #print d[v[0]]  #we do v[0] because we just want the vertex name of the tuple
        #print d[u]
        if d[v[0]] > d[u] + v[1]:
            d[v[0]] = d[u] + v[1]  #after this assignment we need to let all the other nodes know
print d
            





