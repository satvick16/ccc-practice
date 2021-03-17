import sys

N, W = map(int, sys.stdin.readline().split())

val = [0 for i in range(N)]
wt = [0 for i in range(N)]

for i in range(N):
    wi, vi = map(int, input().split())
    wt[i] = wi
    val[i] = vi

dp = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(N+1):
    for w in range(W+1):
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif wt[i-1] <= w:
            dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

sys.stdout.write(str(dp[-1][-1]) + "\n")
