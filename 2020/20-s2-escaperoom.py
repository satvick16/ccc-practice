import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

room = [[] for i in range(M)]

for i in range(M):
    room[i] = list(map(int, sys.stdin.readline().split()))

q = [[0, 0]]
visited = [[False for i in range(N)] for j in range(M)]
visited[0][0] = True

while len(q) > 0:
    s = q.pop(0)

    if room[s[0]][s[1]] == M * N:
        print("yes")
        sys.exit()

    neighbours = []

    for i in range(1, int(room[s[0]][s[1]] ** 0.5 + 1)):
        if room[s[0]][s[1]] % i == 0:
            if i-1 < M and int((room[s[0]][s[1]] / i) - 1) < N:
                neighbours.append([i-1, int((room[s[0]][s[1]] / i) - 1)])
            if i-1 < N and int((room[s[0]][s[1]] / i) - 1) < M:
                neighbours.append([int((room[s[0]][s[1]] / i) - 1), i-1])

    for n in neighbours:
        if visited[n[0]][n[1]]:
            continue

        visited[n[0]][n[1]] = True
        q.append([n[0], n[1]])

print("no")
