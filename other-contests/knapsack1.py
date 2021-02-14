N, W = map(int, input().split())

items = []

for i in range(N):
    wi, vi = map(int, input().split())
    items.append([wi, vi])

dp = [0 for i in range(W+1)]

