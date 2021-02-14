R, C = map(int, input().split())

K = int(input())

cats = []

for i in range(K):
    cats.append(list(map(int, input().split())))

dp = [[0 for i in range(C+1)] for j in range(R+1)]
dp[R][C] = 1

for i in range(R, 0, -1):
    for j in range(C, 0, -1):
        if [i, j] not in cats:
            neighbours = [[i+1, j], [i, j+1]]

            for n in neighbours:
                if n not in cats:
                    if not(n[0] > R) and not(n[1] > C):
                        dp[i][j] += dp[n[0]][n[1]]

print(dp[1][1])
