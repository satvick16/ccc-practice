import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

K = int(sys.stdin.readline())

choices = [[] for i in range(K)]

for i in range(K):
    x, y = input().split()
    choices[i] = [x, int(y)]

grid = [[False for i in range(0, N+1)] for j in range(M+1)]

for choice in choices:
    if choice[0] == 'R':
        for i in range(1, N+1):
            grid[choice[1]][i] = not(grid[choice[1]][i])
    else:
        for i in range(1, M+1):
            grid[i][choice[1]] = not(grid[i][choice[1]])

counter = 0

for i in range(1, M+1):
    for j in range(1, N+1):
        if grid[i][j]:
            counter += 1

print(counter)
