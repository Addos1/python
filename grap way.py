from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")


edges = [
        ("a", "b", 7),
        ("a", "d", 5),
        ("b", "c", 8),
        ("b", "d", 9),
        ("b", "e", 7),
        ("c", "e", 5),
        ("d", "e", 15),
        ("d", "f", 6),
        ("e", "f", 8),
        ("e", "g", 9),
        ("f", "g", 11)
]

print ("=== Dijkstra ===")
print (edges)
print ("a -> e:")
print (dijkstra(edges, "a", "e"))
print ("f -> g:")
print (dijkstra(edges, "f", "g"))



m=['a',' b', 'c', 'd', 'e', 'f', 'g', 'h']
N = [
	['b', 'c', 'd', 'e', 'f'], # a
	['c', 'e'], # b
	['d'], # c
	['e'], # d
	['f'], # e
	['c', 'g', 'h'], # f
	['f', 'h'], # g
	['f', 'g'] # h
]
for i in reversed(range(1,5)):
    N[i]=[]
for i in reversed(range(6,8)):
    N[i]=[]
