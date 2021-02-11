import sys

N, M = map(int, sys.stdin.readline().split())

room = [[] for j in range(N)]

for i in range(N):
    x = list(input())
    room[i] = x

dots = []
graph = {}

for i in range(N):
    for j in range(M):
        if room[i][j] != "W":        
            graph[(i, j)] = []

            neighbours = [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]

            for neighbour in neighbours:
                if room[neighbour[0]][neighbour[1]] != "W":
                    graph[(i, j)].append([neighbour[0], neighbour[1]])
        
        if room[i][j] == "S":
            start = [i, j]
        if room[i][j] == ".":
            dots.append([i, j])

q = [start]
visited = [[start[0], start[1]]]
distance = [[0 for i in range(M)] for j in range(N)]

distance[start[0]][start[1]] = 0

while len(q) > 0:
    s = q.pop(0)

    for neighbour in graph[tuple(s)]:
        if neighbour in visited:
            continue

        if room[neighbour[0]][neighbour[1]] == ".":
            d = abs(neighbour[0] - s[0] + neighbour[1] - s[1])
            distance[neighbour[0]][neighbour[1]] = distance[s[0]][s[1]] + d
            
        visited.append([neighbour[0], neighbour[1]])
        q.append([neighbour[0], neighbour[1]])

for dot in dots:
    if distance[dot[0]][dot[1]] == 0:
        print(-1)
    else:
        print(distance[dot[0]][dot[1]])
