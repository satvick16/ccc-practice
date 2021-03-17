A = int(input())
B = int(input())

N = int(input())

motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

for i in range(N):
    motels.append(int(input()))

motels.sort()

dp = [0 for i in range(len(motels))]
dp[0] = 1

for i in range(len(motels)):
    if dp[i] > 0:
        for j in range(1, len(motels)):
            if A <= motels[j]-motels[i] <= B:
                dp[j] += dp[i]

print(dp[-1])
