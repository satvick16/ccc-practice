import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

room = []

for i in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    room.append(row)

location = [1, 1]
path = []
visited = []

def solve(location, path, visited):
    if location[0] == M and location[1] == N:
        return True

    visited.append(location)

    val = room[location[0] - 1][location[1] - 1]

    for i in range(M):
        for j in range(N):
            if val == (i+1) * (j+1) and not([i+1, j+1] in visited):
                if solve([i+1, j+1], path, visited):
                    path.append(location)
                    return True

    return False

if solve(location, path, visited):
    print("yes")
else:
    print("no")
