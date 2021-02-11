R, C = map(int, input().split())

K = int(input())

cats = []

for i in range(K):
    cats.append(list(map(int, input().split())))

ways = [[0 for i in range(-1, C)] for j in range(-1, R)]
ways[R][C] = 1
