import sys

N, M = map(int, sys.stdin.readline().split())

comps = [[0, 0] for i in range(M)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    comps[i] = [x, y]

graph = {}

for comp in comps:
    graph[comp[0]] = []
    graph[comp[1]] = []

for comp in comps:
    graph[comp[0]].append(comp[1])

p, q = map(int, sys.stdin.readline().split())

def bfs(graph, start, target, N):
    q = []
    visited = [False for i in range(N)]

    visited[start-1] = True
    q.append(start)

    while len(q) > 0:
        s = q.pop(0)

        for child in graph[s]:
            if child == target:
                return True
            
            if visited[child-1]:
                continue

            visited[child-1] = True
            q.append(child)

    return False

if bfs(graph, p, q, N):
    print("yes")
    sys.exit()

if bfs(graph, q, p, N):
    print("no")
    sys.exit()

print("unknown")
