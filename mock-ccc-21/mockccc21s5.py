from itertools import combinations

N, M = map(int, input().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vertices = [i for i in range(1, N+1)]

subsets = []
