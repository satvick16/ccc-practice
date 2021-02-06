import sys

N, M = map(int, sys.stdin.readline().split())

comps = []

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    comps.append([x, y])

p, q = map(int, sys.stdin.readline().split())

graph = {}

for comp in comps:
    graph[comp[0]] = []
    graph[comp[1]] = []

for comp in comps:
    graph[comp[0]].append(comp[1])

def bfs(graph, start, target, N):
    q = []
    visited = []

    visited.append(start)
    q.append(start)

    while len(q) > 0:
        s = q.pop(0)

        for child in graph[s]:
            if child == target:
                return True
            
            if child in visited:
                continue

            visited.append(child)
            q.append(child)

    return False

if bfs(graph, p, q, N):
    print("yes")
    sys.exit()

if bfs(graph, q, p, N):
    print("no")
    sys.exit()

print("unknown")
