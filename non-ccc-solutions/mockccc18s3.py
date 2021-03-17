import copy

N, M = map(int, input().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

edges = []

for i in range(M):
    si, ti = map(int, input().split())
    graph[si].append(ti)
    edges.append([si, ti])

def bfs(graph, N):
    queue = []
    visited = []
    distance = [0 for i in range(len(graph))]

    start = 1
    visited.append(1)
    distance[start-1] = 0
    queue.append(start)

    while len(queue) > 0:
        s = queue.pop(0)

        for neighbour in graph[s]:
            if neighbour in visited:
                continue

            if neighbour == N:
                return True

            visited.append(neighbour)
            distance[neighbour-1] = distance[s-1] + 1
            queue.append(neighbour)

    return False

for edge in edges:
    graph_copy = copy.deepcopy(graph)
    graph_copy[edge[0]].remove(edge[1])

    if bfs(graph_copy, N):
        print("YES")
    else:
        print("NO")
