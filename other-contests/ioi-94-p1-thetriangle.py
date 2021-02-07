N = int(input())

triangle = []

for i in range(1, N+1):
    triangle.append(list(map(int, input().split())))

highest_sum = [[0 for j in range(i)] for i in range(1, N+1)]

highest_sum[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            highest_sum[i][j] = triangle[i][j] + highest_sum[i-1][0]
        elif j == i:
            highest_sum[i][j] = triangle[i][j] + highest_sum[i-1][-1]
        else:
            highest_sum[i][j] = triangle[i][j] + max(highest_sum[i-1][j-1], highest_sum[i-1][j])

print(max(highest_sum[-1]))
