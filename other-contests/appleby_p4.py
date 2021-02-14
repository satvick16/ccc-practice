import sys

N, M = map(int, sys.stdin.readline().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    ai, bi = map(int, sys.stdin.readline().split())
    graph[ai].append(bi)
    graph[bi].append(ai)

# looking for cycles of size >3 in graph

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

cycles = [([node]+path)[1:] for node in graph for path in dfs(graph, node, node) if len(([node]+path)[1:]) >= 3]

if len(cycles) > 0:
    print(len(min(cycles)))
    for i in range(len(min(cycles))):
        print(min(cycles)[i], end=" ")
    print()
else:
    print(-1)
