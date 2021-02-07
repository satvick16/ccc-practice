N, M = map(int, input().split())
rs = list(map(int, input().split()))

paths = []

for i in range(N-1):
    ai, bi = map(int, input().split())
    paths.append([ai, bi])

adj = {}

for i in range(N):
    adj[i] = []

for i in paths:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])

queue = []
visited = []
distance = [0 for i in range(len(adj))]

start = 1
visited2.append(1)
distance[start-1] = 0
queue.append(start)

while len(queue) > 0:
    s = queue.pop(0)
    print(s)

    for neighbour in graph2[s]:
        if neighbour in visited2:
            continue

        visited2.append(neighbour)
        distance[neighbour-1] = distance[s-1] + 1
        queue.append(neighbour)
