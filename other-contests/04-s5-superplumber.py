grids = []

while True:
    m, n = map(int, input().split())

    if m == n == 0:
        break
    else:
        grid = []
        
        for i in range(m):
            row = list(input())

            for r in range(len(row)):
                if row[r] == ".":
                    row[r] = 0
                else:
                    if 49 <= ord(row[r]) <= 57:
                        row[r] = int(row[r])

            grid.append(row)

        grids.append(grid)

for grid in grids:
    dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    dp[len(dp)-1][0] = grid[len(dp) - 1][0]

    for i in range(len(grid)-2, -1, -1):
        if grid[i][0] >= 0:
            dp[i][0] = dp[i+1][0] + grid[i][0]
        else:
            break

    for c in range(1, len(grid[0])):

        for r in range(len(grid)):
            if dp[r][c-1] != '*':
                t = dp[r][c-1]
                for k in range(r, len(grid)):
                    if grid[k][c] != '*':
                        t += grid[k][c]
                        if t > dp[k][c]:
                            dp[k][c] = t
                    else:
                        break

        for r in range(len(grid)-1, -1, -1):
            if dp[r][c-1]!= '*':
                t = dp[r][c-1]
                for k in range(r, -1, -1):
                    if grid[k][c] != '*':
                        t += grid[k][c]
                        if t > dp[k][c]:
                            dp[k][c] = t
                    else:
                        break

    print(dp[-1][-1])
