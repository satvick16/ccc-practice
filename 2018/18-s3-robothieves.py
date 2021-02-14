import sys

N, M = map(int, sys.stdin.readline().split())

room = [[] for j in range(N)]

for i in range(N):
    x = list(input())
    room[i] = x

blacklist = [[True for i in range(M)] for j in range(N)]

for i in range(N):
    for j in range(M):
        if room[i][j] == "W":
            continue
        else:
            if room[i][j] == "C":
                blacklist[i][j] = False
                for k in range(i+1, N):
                    if room[k][j] == "W":
                        break
                    else:
                        blacklist[k][j] = False
                for m in range(i, 0, -1):
                    if room[m][j] == "W":
                        break
                    else:
                        blacklist[m][j] = False

                for n in range(j+1, M):
                    if room[i][n] == "W":
                        break
                    else:
                        blacklist[i][n] = False
                for p in range(j, 0, -1):
                    if room[i][p] == "W":
                        break
                    else:
                        blacklist[i][p] = False

dots = []
graph = {}

for i in range(N):
    for j in range(M):
        if room[i][j] != "W" and blacklist[i][j]:        
            graph[(i, j)] = []

            neighbours = [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]

            for neighbour in neighbours:
                if room[neighbour[0]][neighbour[1]] != "W" and blacklist[i][j]:
                    graph[(i, j)].append([neighbour[0], neighbour[1]])
        
        if room[i][j] == "S":
            start = [i, j]
        if room[i][j] == ".":
            dots.append([i, j])

q = [start]
visited = [[False for i in range(M)] for j in range(N)]
distance = [[0 for i in range(M)] for j in range(N)]

distance[start[0]][start[1]] = 0

while len(q) > 0:
    s = q.pop(0)

    for neighbour in graph[tuple(s)]:
        if visited[neighbour[0]][neighbour[1]]:
            continue

        if room[neighbour[0]][neighbour[1]] == ".":
            d = abs(neighbour[0] - s[0] + neighbour[1] - s[1])
            distance[neighbour[0]][neighbour[1]] = distance[s[0]][s[1]] + d
            
        visited[neighbour[0]][neighbour[1]] = True
        q.append([neighbour[0], neighbour[1]])

for dot in dots:
    if distance[dot[0]][dot[1]] == 0:
        print(-1)
    else:
        print(distance[dot[0]][dot[1]])
