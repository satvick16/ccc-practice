import math

start = 1

distance = [math.inf for i in range(n)]
distance[start-1] = 0

q = []
q.append([0, start])

visited = [False for i in range(n)]
visited[start-1] = True

while len(q) > 0:
    a = q[0][1]
    q.pop(0)

    if visited[a]:
        continue

    visited[a] = True

    for neighbour in graph[a]:
        b = i[0]
        w = i[1]

        if distance[a]+w < distance[b]:
            distance[b] = distance[a] + w
            q.append([-1 * distance[b], b])

print(distance)
