N = 10000

dp = [99999999 for i in range(N+1)]
dp[1] = 0

for i in range(1, N+1):
    if not(i+1 > N):
        dp[i+1] = min(dp[i+1], dp[i]+1)
    if not(i*2 > N):
        dp[i*2] = min(dp[i*2], dp[i]+1)
    if not(i*3 > N):
        dp[i*3] = min(dp[i*3], dp[i]+1)

print(dp[-1])
