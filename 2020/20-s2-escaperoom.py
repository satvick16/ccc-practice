import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

room = []

for i in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    room.append(row)

room[-1].append(-99999999999)

q = []
visited = []

start = [0, 0]
visited.append(start)
q.append(start)

while len(q) > 0:
    s = q.pop(0)

    if room[][] == -99999999999:
        print("yes")
        sys.exit()

    neighbours = []

    for i in range(M):
        for j in range(N):
            if room[s[0]][s[1]] / i == j:
                neighbours.append([i, j])

    for neighbour in neighbours:
        if neighbour in visited:
            continue

        visited.append(neighbour)
        q.append(neighbour)

print("no")













##location = [1, 1]
##path = []
##visited = []
##
##def solve(location, path, visited):
##    if location[0] == M and location[1] == N:
##        return True
##
##    visited.append(location)
##
##    val = room[location[0] - 1][location[1] - 1]
##
##    for i in range(M):
##        for j in range(N):
##            if val == (i+1) * (j+1) and not([i+1, j+1] in visited):
##                if solve([i+1, j+1], path, visited):
##                    path.append(location)
##                    return True
##
##    return False
##
##if solve(location, path, visited):
##    print("yes")
##else:
##    print("no")
