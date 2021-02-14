'''
N = 4
nums = [1, 2, 3]

dp = [0 for i in range(N+1)]
dp[0] = 1

for i in range(1, len(dp)):
    for num in nums:
        dp[i] += dp[i-num]

print(dp)
'''

################################################

'''
coins = [1, 2, 5]
N = 11

dp = [99999999 for i in range(N+1)]
dp[0] = 0

for i in range(1, len(dp)):
    for coin in coins:
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp)
'''

################################################

coins = [1, 2, 5]
N = 5

dp = [[0 for j in range(len(coins))] for i in range(N+1)]
dp[0] = [1 for i in range(len(coins))]

