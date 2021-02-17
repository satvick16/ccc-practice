import sys

R = int(sys.stdin.readline())
L = int(sys.stdin.readline())

grid = [[] for i in range(R)]

for i in range(R):
    grid[i] = list(map(int, sys.stdin.readline().split()))

    for x in range(len(grid[i])):
        if grid[i][x]:
            grid[i][x] = True
        else:
            grid[i][x] = False

foos = [grid[0]]

for i in range(1, R):

    x = []

    for j in foos:
        a = [False for i in range(L)]

        for k in range(L):
            a[k] = grid[i][k] ^ j[k]

        x.append(a)
        x.append(grid[i])

    foos = list(set(tuple(elem) for elem in x))

print(len(list(set(tuple(elem) for elem in foos))))
