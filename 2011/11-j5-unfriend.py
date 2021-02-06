N = int(input())

tree = {}

for i in range(1, N+1):
    tree[i] = []

for i in range(1, N):
    j = int(input())
    tree[j].append(i)

sets = [[]]

def bfs(graph, start):
    q = []
    visited = []

    visited.append(start)
    q.append(start)

    while len(q) > 0:
        s = q.pop(0)

        for child in graph[s]:
            if child in visited:
                continue

            visited.append(child)
            q.append(child)

    return visited

nones = {}

for x, y in tree.items():
    if y == []:
        nones[] = 
    else:
        pass
